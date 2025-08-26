from enum import Enum
from htmlnode import *
from split_nodes import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    if block[0:2] == "# " or block[0:3] == "## " or block[0:4] == "### " or block[0:5] == "#### " or block[0:6] == "##### " or block[0:7] == "###### ":
        return BlockType.HEADING
    if block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    lines = block.split("\n")
    line_start = ""
    for line in lines:
        if line_start == "":
            if line[0] == ">":
                line_start = ">"
            elif line[0:2] == "- ":
                line_start = "- "
            elif line[0:3] == "1. ":
                line_start = "1. "
            else:
                return BlockType.PARAGRAPH
        elif len(line_start) == 1 and line[0] != line_start:
            return BlockType.PARAGRAPH
        elif len(line_start) == 2 and line[0:2] != line_start:
            return BlockType.PARAGRAPH
        elif len(line_start) == 3:
            if str(int(line_start[0]) + 1) + ". " != line[0:3]:
                return BlockType.PARAGRAPH
            line_start = line[0:3]
    if line_start == ">":
        return BlockType.QUOTE
    elif line_start == "- ":
        return BlockType.UNORDERED_LIST
    return BlockType.ORDERED_LIST

def markdown_to_blocks(markdown):
    return list(map(lambda x: x.strip(), markdown.strip().split("\n\n")))

def text_to_children(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            splits = block.split(" ", 1)
            children.append(ParentNode("h"+str(len(splits[0])), text_to_children(splits[1])))
        if block_type == BlockType.CODE:
            children.append(ParentNode("pre",[LeafNode("code", block[4:-3])]))
        if block_type == BlockType.QUOTE:
            splits = block.split("\n")
            lines = ""
            for split in splits:
                lines += split[2:] + "\n"
            children.append(ParentNode("blockquote", text_to_children(lines)))
        if block_type == BlockType.PARAGRAPH:
            children.append(ParentNode("p", text_to_children(block.replace("\n", " "))))
        if block_type == BlockType.ORDERED_LIST:
            splits = block.split("\n")
            lines = []
            for split in splits:
                lines.append(ParentNode("li", text_to_children(split[3:])))
            children.append(ParentNode("ol", lines))
        if block_type == BlockType.UNORDERED_LIST:
            splits = block.split("\n")
            lines = []
            for split in splits:
                lines.append(ParentNode("li", text_to_children(split[2:])))
            children.append(ParentNode("ul", lines))
    html = ParentNode("div", children)
    return html

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block[0:2] == "# ":
            return block[2:].strip()
    raise Exception("No title found.")