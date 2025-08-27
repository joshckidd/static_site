from textnode import *
from split_blocks import *
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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as file:
        template = file.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    if not os.path.isdir(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as file:
        template = file.write(html)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        if os.path.isfile(os.path.join(dir_path_content, file)):
            generate_page(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file.split(".")[0] + ".html"))
        else:
            generate_pages_recursive(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file))

def main():
    generate_site()
    generate_pages_recursive("content/", "template.html", "public/")

main()