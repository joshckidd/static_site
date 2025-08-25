import unittest
from split_blocks import *

class TestSplitBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_block_to_blocktype(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

# This is a header

## This is also a header

### This too is a header

#### Still a header

##### Still a header!

###### Still a header!

####### PAragraph!

#Also paragraph

>This is quote
>By Joshua Kidd

>This is not a quote
Because not all lines start with >

```
This is a code block.
```

1. This is a list
2. With numbered items

- This is a list
- with items

-This is not a list
- There needs to be a space

2. This is also not a list
3. The numbers aren't in order
4. It's a paragraph instead
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(block_to_block_type(blocks[0]), BlockType.PARAGRAPH)
            self.assertEqual(block_to_block_type(blocks[1]), BlockType.PARAGRAPH)
            self.assertEqual(block_to_block_type(blocks[2]), BlockType.HEADING)
            self.assertEqual(block_to_block_type(blocks[3]), BlockType.HEADING)
            self.assertEqual(block_to_block_type(blocks[4]), BlockType.HEADING)
            self.assertEqual(block_to_block_type(blocks[5]), BlockType.HEADING)
            self.assertEqual(block_to_block_type(blocks[6]), BlockType.HEADING)
            self.assertEqual(block_to_block_type(blocks[7]), BlockType.HEADING)
            self.assertEqual(block_to_block_type(blocks[8]), BlockType.PARAGRAPH)
            self.assertEqual(block_to_block_type(blocks[9]), BlockType.PARAGRAPH)
            self.assertEqual(block_to_block_type(blocks[10]), BlockType.QUOTE)
            self.assertEqual(block_to_block_type(blocks[11]), BlockType.PARAGRAPH)
            self.assertEqual(block_to_block_type(blocks[12]), BlockType.CODE)
            self.assertEqual(block_to_block_type(blocks[13]), BlockType.ORDERED_LIST)
            self.assertEqual(block_to_block_type(blocks[14]), BlockType.UNORDERED_LIST)
            self.assertEqual(block_to_block_type(blocks[15]), BlockType.PARAGRAPH)
            self.assertEqual(block_to_block_type(blocks[16]), BlockType.PARAGRAPH)
             