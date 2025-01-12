from markdown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_blocktype


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_blocktype(block)
        print(block_type)
        print(block)






    return markdown_blocks
















# testing area

test_markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

test = markdown_to_html_node(test_markdown)
print(test)