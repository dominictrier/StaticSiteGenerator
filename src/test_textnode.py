import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNODE, LeafNode, ParentNode


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

    def test_textnode_to_htmlnode_link_assert(self):
        node = TextNode("this is an anchor text", TextType.LINK, "https://www.examplelink.com")
        leafnode = node.textnode_to_htmlnode().to_html()
        assert leafnode == '<a href="https://www.examplelink.com">this is an anchor text</a>'

    def test_textnode_to_htmlnode_image_assert(self):
        node = TextNode("this is an exmaple alt text", TextType.IMAGE, "https://www.examplelink.com/image.jpg")
        leafnode = node.textnode_to_htmlnode().to_html()
        assert leafnode == '<img src="https://www.examplelink.com/image.jpg" alt="this is an exmaple alt text"/>'


if __name__ == "__main__":
    unittest.main()
