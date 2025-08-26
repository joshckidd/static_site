from textnode import *
import os, shutil

def copy_file(path, files):
    for file in files:
        if os.path.isfile(os.path.join("static/", path, file)):
            shutil.copy(os.path.join("static/", path, file), os.path.join("public/", path, file))
        else:
            os.mkdir(os.path.join("public/", path, file))
            copy_file(os.path.join(path, file), os.listdir(os.path.join("static/", path, file)))

def generate_site():
    if os.path.exists("public/"):
        shutil.rmtree("public/")
    os.mkdir("public/")
    copy_file("", os.listdir("static/"))
    

def main():
    generate_site()

main()