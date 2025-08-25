from enum import Enum

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
    return list(map(lambda x: x.strip(), markdown.split("\n\n")))