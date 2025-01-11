from markdown_to_blocks import markdown_to_blocks


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)






    return markdown_blocks
















# testing area

test_markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""

test = markdown_to_html_node(test_markdown)
print(test)