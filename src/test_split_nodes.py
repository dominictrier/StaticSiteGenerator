import unittest
from split_nodes import split_nodes_images, split_nodes_links
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_images_basic(self):
        test_node = TextNode(
            "Here is some text with an ![image](test.jpg) in the middle and another ![photo](pic.png) near the end.",
            TextType.NORMAL
            )
        
        result = split_nodes_images([test_node])

        expected = [
            TextNode("Here is some text with an ", TextType.NORMAL, None),
            TextNode("image", TextType.IMAGE, "test.jpg"),
            TextNode(" in the middle and another ", TextType.NORMAL, None),
            TextNode("photo", TextType.IMAGE, "pic.png"),
            TextNode(" near the end.", TextType.NORMAL, None)
            ]

        self.assertEqual(result,expected, "Test failed: test_split_nodes_image_basic")


    def test_split_nodes_link_basic(self):
        test_node = TextNode(
             "Here is a [link to somewhere](https://test.com) and [another link](https://example.com) in text.",
             TextType.NORMAL
             )
        
        result = split_nodes_links([test_node])

        expected = [
            TextNode("Here is a ", TextType.NORMAL, None),
            TextNode("link to somewhere", TextType.LINK, "https://test.com"),
            TextNode(" and ", TextType.NORMAL, None),
            TextNode("another link", TextType.LINK, "https://example.com"),
            TextNode(" in text.", TextType.NORMAL, None)
            ]

        self.assertEqual(result,expected, "Test failed: test_split_nodes_links_basic")
