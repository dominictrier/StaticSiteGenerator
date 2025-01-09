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

        expected = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block',
            '* This is a list item',
            '* This is another list item'
            ]

        self.assertEqual(result, expected,"Test failed: test_bold_italic_markdown")



if __name__ == "__main__":
    unittest.main()