import os
import shutil


def delete_all_content(dir: str):
    if not dir:
        raise Exception("no directory provided")
    if not os.path.exists(dir):
        raise Exception("directory does not exists")
    dir_content = os.listdir(dir)
    for item in dir_content:
        path = os.path.join(dir, item)
        if os.path.isfile(path):
            os.remove(path)
        if os.path.isdir(path):
            shutil.rmtree(path)
    print(f"content of directory {dir} sucessfully deleted")


def print_files_in_dir(dir: str):
    dir_content = os.listdir(dir)
    for item in dir_content:
        full_path = os.path.join(dir, item)
        print(full_path)


def move_folder_cotent(source, target):
    if target.path.exists():
        target_dir_content = target.listdir()
    if len(target_dir_content) > 0:
        pass
        

def main():
    static = "./static/"
    public = "./public/"
    testing = "./testing"



if __name__ == "__main__":
    main()


