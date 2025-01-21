import os
import shutil


def delete_all_content(dir: str):
    if not dir:
        raise Exception("no directory provided")
    if not os.path.exists(dir):
        raise Exception("directory does not exists")
    dir_content = os.listdir(dir)
    for item in dir_content:
        if os.path.isfile(item):
            os.remove(item)
        if os.path.isdir(item):
            shutil.rmtree(item)
    print(f"content of directory {dir} sucessfully deleted")





def move_folder_cotent(source, target):
    if target.path.exists():
        target_dir_content = target.listdir()
    if len(target_dir_content) > 0:
        pass
        

def main():
    static = "./static/"
    public = "./public/"
    dir_static = os.listdir(static)
    dir_public = os.listdir(public)
    for item in dir_static:
        print(f'static {item}')

    for item in dir_public:
        print(f'public {item}')


if __name__ == "__main__":
    main()


