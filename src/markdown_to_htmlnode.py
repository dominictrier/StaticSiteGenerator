from markdown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_blocktype
from htmlnode import HTMLNODE, LeafNode, ParentNode


def markdown_to_html_node(markdown):
    htmlnodes = []
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_blocktype(block)
        if block_type == "heading":
            result = header_to_html(block)
            htmlnodes.append(result)
        if block_type == "code":
            result = 








    return "nothing"



def header_to_html(markdown):
    text = markdown.split(" ", 1)
    amount = text[0].count("#")
    node = LeafNode(f'h{amount}', text[1])
    
    return node


def code_to_html(markdown):
    text = 
    
















# testing area

test_markdown = """### This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

test = markdown_to_html_node(test_markdown)
print(test)