import unittest

from textnode import TextNode, TextType

# print("TextNode imported successfully!")

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


if __name__ == "__main__":
    unittest.main()
