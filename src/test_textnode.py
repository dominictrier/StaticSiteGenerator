import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNODE, LeafNode, ParentNode

# print("TextNode imported successfully!")


# Test Text Node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_isUrl(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_texttype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_textnode_initialized(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        assert node.text == "This is a text node"
        assert node.text_type == TextType.LINK
        assert node.url == "https://example.com"

    def test_textnode_repr(self):
        node = TextNode("Hello", TextType.NORMAL)
        assert repr(node) == "TextNode(Hello, normal, None)"

    def test_textnode_empty_text(self):
        empty_node = TextNode("", TextType.NORMAL)
        assert empty_node.text == ""
        assert empty_node.text_type == TextType.NORMAL
        assert empty_node.url is None


    # Test TextNode to HTMLNode

    def test_textnode_to_htmlnode_assert(self):
        empty_textnode = TextNode("this is an exmaple alt text", TextType.LINK, "https://www.examplelink.com")
        new_leafnode = empty_textnode.textnode_to_htmlnode()
        print (new_leafnode)


if __name__ == "__main__":
    unittest.main()
