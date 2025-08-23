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


def main():
    tn = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(tn)

main()