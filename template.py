import os


dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "savedmodels",
    "src"
]

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")

]

for dir_ in dirs :
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"),"w") as f :
        pass

for file_ in files :
    with open(file_,"w") as f :
        pass