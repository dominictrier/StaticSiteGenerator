import os
import shutil
import markdown_to_htmlnode
from htmlnode import ParentNode

def clean_dir(dir: str):
    if not os.path.exists(dir):
        raise Exception("directory does not exist")
    dir_content = os.listdir(dir)
    for item in dir_content:
        path = os.path.join(dir, item)
        if os.path.isfile(path):
            os.remove(path)
        if os.path.isdir(path):
            shutil.rmtree(path)


# helper print function
def print_files_in_dir(dir: str):
    dir_content = os.listdir(dir)
    for item in dir_content:
        full_path = os.path.join(dir, item)
        print(full_path)


def recursive_copy_content(source: str, target: str):
    dir_content = os.listdir(source)
    for item in dir_content:
        path_source = os.path.join(source, item)
        path_target = os.path.join(target, item)
        if os.path.isfile(path_source):
            shutil.copy(path_source, path_target)
        if os.path.isdir(path_source):
            os.mkdir(os.path.join(target, item))
            recursive_copy_content(os.path.join(source, item), os.path.join(target, item))


def assure_exists(dir: str, create: str = "no"):
    if os.path.exists(dir):
        return True
    else:
        if create == "yes":
            os.mkdir(dir)
            return True  
    return False


def dir_isempty(dir: str):
    dir_content = os.listdir(dir)
    if not dir_content:
        return True
    return False


def exctract_title(markdown):
    line_rows = markdown.splitlines()
    for line in line_rows:
        if line.startswith("# "):
            return line.split(" ", 1)[1]
    raise Exception("no h1 Headline found")


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r', encoding='utf-8') as f:
        raw_markdown = f.read()
    with open(template_path, 'r', encoding='utf-8') as t:
        raw_template = t.read()
    markdown_html = markdown_to_htmlnode.markdown_to_html_node(raw_markdown)
    markdown_headline = exctract_title(raw_markdown)
    print(markdown_headline)
    print(markdown_html)
    updated_template = raw_template.replace('{{ Title }}', markdown_headline)
    updated_template = updated_template.replace('{{ Content }}', markdown_html.to_html())
    with open(dest_path, 'w') as d:
        d.write(updated_template)


def main():
    source = "./static/"
    target = "./public/"
    source_path = "./content/index.md"
    temp_path = "./template.html"
    dest_path = "./public/index.html"
    assure_exists(target, "yes")
    if not assure_exists(source):
        raise Exception("no source directory")
    if dir_isempty(source):
        raise Exception("source is empty")
    if not dir_isempty(target):
        clean_dir(target)
    recursive_copy_content(source, target)
    clean_dir(source)
    #print(os.path.dirname(dest_path))
    #os.makedirs(os.path.dirname(dest_path))
    generate_page(source_path, temp_path, dest_path)


if __name__ == "__main__":
    main()


