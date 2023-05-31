import os

from markdown import markdown

stack: list = ["readme_files"]
files: list = []

# A recursive loop to get all the readme files in the `readme_files` tree.
while stack:
    for path in stack:
        for file in os.listdir(path):
            # If it's another dir, add it to the stack for recursion.
            if os.path.isdir(f"{path}/{file}"):
                stack.append(f"{path}/{file}")
            
            # If it's a readme file add it to the files list.
            elif file.split(".")[-1] == "md":
                files.append(f"{path}/{file}")
        
        stack.pop(0)

print(files)


for file in files:
    with open(file, "r", encoding="utf-8") as f:
        html: str = markdown(f.read())

    paths_list: list = file.split("/")
    print(paths_list)
    paths_list[0] = "docs"

    full_dir: str = ""

    for folder in paths_list[0:-1]:
        full_dir += f"{folder}/"

        if not os.path.isdir(full_dir):
            os.mkdir(full_dir)

    print(f"{'/'.join(paths_list[0:-1])}/{paths_list[-1]}")
    with open(f"{'/'.join(paths_list[0:-1])}/{paths_list[-1]}", "w", encoding="utf-8") as f:
        print(f.closed)
        f.write(html)
        

print(files)