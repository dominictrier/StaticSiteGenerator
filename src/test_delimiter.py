import unittest

from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_multiple_split(self):
        old_nodes = [
            TextNode("This has a **bold** and a *italic* word", TextType.NORMAL)
            ]
        delimiter = '**'
        text_type = TextType.BOLD

        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        expected = [
            TextNode("This has a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" and a *italic* word", TextType.NORMAL)
        ]

        self.assertEqual(result,expected, "Test failed: did not match expected result")


    def test_simple_split(self):
        old_nodes = [TextNode("This has a `code` segment", TextType.NORMAL)]
        delimiter = "`"
        text_type = TextType.CODE

        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        expected = [
            TextNode("This has a ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" segment", TextType.NORMAL)
    ]
        self.assertEqual(result, expected, "Test failed: did not match expected result")



if __name__ == "__main__":
    unittest.main()