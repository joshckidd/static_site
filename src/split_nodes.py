from textnode import *
from htmlnode import *
import re

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"alt": text_node.text, "src": text_node.url})
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if delimiter not in node.text or node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            in_delimited_text = False
            text_splits = node.text.split(delimiter)
            for split in text_splits:
                if in_delimited_text == False:
                    if split != '':
                        new_nodes.append(TextNode(split, TextType.TEXT))
                    in_delimited_text = True
                else:
                    if split != '':
                        new_nodes.append(TextNode(split, text_type))
                    in_delimited_text = False
            if in_delimited_text == False:
                raise Exception("Invalid markdown.")
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
        else:
            current_text = node.text
            for image in images:
                splits = current_text.split(f"![{image[0]}]({image[1]})", 1)
                if splits[0] != "":
                    new_nodes.append(TextNode(splits[0], TextType.TEXT))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                current_text = splits[1]
            if current_text != "":
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
        else:
            current_text = node.text
            for link in links:
                splits = current_text.split(f"[{link[0]}]({link[1]})", 1)
                if splits[0] != "":
                    new_nodes.append(TextNode(splits[0], TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                current_text = splits[1]
            if current_text != "":
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    bold_nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
    image_nodes = split_nodes_image(code_nodes)
    link_nodes = split_nodes_link(image_nodes)
    return link_nodes