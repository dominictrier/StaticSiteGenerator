import unittest
from markdown_to_blocks import markdown_to_blocks


class TestTextToTextNodes(unittest.TestCase):
    def test_bold_italic_markdown(self):
        test_markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        result = markdown_to_blocks(test_markdown)

        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(result, expected,"Test failed: test_bold_italic_markdown")


    def test_multiple_blank_lines(self):
        test_markdown = """# First block


    Second block"""
        expected = ["# First block", "Second block"]
        result = markdown_to_blocks(test_markdown)
        self.assertEqual(result, expected, "Multiple blank lines should be treated as one")


    def test_whitespace_stripping(self):
        test_markdown = """   # Heading with space   

        This has indent.    """
        expected = ["# Heading with space", "This has indent."]
        result = markdown_to_blocks(test_markdown)
        self.assertEqual(result, expected, "Leading/trailing whitespace should be stripped")


    def test_empty_blocks(self):
        test_markdown = """# First

        
        
    Second"""
        expected = ["# First", "Second"]
        result = markdown_to_blocks(test_markdown)
        self.assertEqual(result, expected, "Empty blocks should be removed")


    def test_single_block(self):
        test_markdown = "This is just one block"
        expected = ["This is just one block"]
        result = markdown_to_blocks(test_markdown)
        self.assertEqual(result, expected, "Single block should work")


if __name__ == "__main__":
    unittest.main()