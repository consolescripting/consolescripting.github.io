import os

from markdown import markdown

def compile_files(input_dir: str, output_dir: str) -> None:
    stack: list = [input]
    files: list = []

    # A recursive loop to get all the readme files in the `readme_files` tree.
    while stack:
        for path in stack:
            for file in os.listdir(path):
                # If it's another dir, add it to the stack for recursion.
                if os.path.isdir(f"{path}/{file}"):
                    stack.append(f"{path}/{file}")
                
                # If it's a readme file add it to the files list.
                elif file.split(".")[-2] == "md":
                    files.append(f"{path}/{file}")
            
            stack.pop(-1)


    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            html: str = markdown(f.read())

        paths_list: list = file.split("/")
        paths_list[0] = output_dir

        full_dir: str = ""

        for folder in paths_list[0:-1]:
            full_dir += f"{folder}/"

            if not os.path.isdir(full_dir):
                os.mkdir(full_dir)

        with open(f"{'/'.join(paths_list[0:-1])}/{paths_list[-1].replace('.md', '.html')}", "w", encoding="utf-8") as f:
            f.write(html)
            
    print(f"Compiled files!")


def create_web_list(input_dir: str) -> None:
    stack: list = [input_dir]
    files: list = []
    dirs: list =  []

    while stack:
        for path in stack:
            for file in os.listdir(path):
                if os.path.isdir(file):
                    for l in [stack, dirs]:
                        l.append(f"{path}/{file}")
                
                elif file.split(".")[-1] == "md":
                    files.append(f"{path}/{file}")
            
            stack.pop(0)
    

    markdown_string: str = ""
    tree: dict = {}

    for file in files:
        paths: list = file.split("/")[0:-1]
        current_tree: dict = tree

        for path in paths:
            if current_tree.get(path):
                current_tree = current_tree[path]
            
            else:
                current_tree[path] = {"files": []}
                current_tree = current_tree[path]
        
        if current_tree.get("files"):
            current_tree["files"].append(paths[-1])
        
        else:
            current_tree["files"] = paths[-1]

        print(current_tree)
    

create_web_list("readme_files")




