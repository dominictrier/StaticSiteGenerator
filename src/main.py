import os
import shutil


def assure_empty(dir: str):
    if not dir:
        raise Exception("no directory provided")
    if not os.path.exists(dir):
        raise Exception("directory does not exists")
    dir_content = os.listdir(dir)
    if dir_content == []:
        print("directory is empty .. nothing todo")
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

def assure_target(dir: str):
    if os.path.exists(dir):
        print("directory exists, nothing todo")
    if not os.path.exists(dir):
        print("directory does not exists ... creating")
        os.mkdir(dir)
        

def main():
    static = "./static/"
    public = "./public/"
    testing = "./testing"
    assure_target(public)
    assure_empty(public)





if __name__ == "__main__":
    main()


