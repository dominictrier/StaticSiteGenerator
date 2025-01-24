import os
import shutil


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


def main():
    source = "./static/"
    target = "./public/"
    assure_exists(target, "yes")
    if not assure_exists(source):
        raise Exception("no source directory")
    if dir_isempty(source):
        raise Exception("source is empty")
    if not dir_isempty(target):
        clean_dir(target)
    recursive_copy_content(source, target)
    clean_dir(source)


if __name__ == "__main__":
    main()


