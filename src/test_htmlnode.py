import unittest

from htmlnode import HTMLNODE, LeafNode, ParentNode

# print("HTMLNODE imported successfully!")


class TestHTMLNODE(unittest.TestCase): #node = HTMLNODE("a", "this is an example text", None, {"href": "https://www.google.com", "target": "_blank"})

    # Test HTMLNODE

    def test_HTMLNODE_eq(self):
        node = HTMLNODE("a", "this is an example text", None)
        node2 = HTMLNODE("a", "this is an example text", None)
        self.assertEqual(node, node2)

    def test_HTMLNODE_noteq(self):
        node = HTMLNODE("a", "this is an example text", None)
        node2 = HTMLNODE("b", "this is an example text", None)
        self.assertNotEqual(node, node2)

    def test_HTMLNODE_initialization_with_all_attributes(self):
        node = HTMLNODE("a", "link text", [HTMLNODE("span", "child")], {"href": "https://example.com"})
        assert node.tag == "a"
        assert node.value == "link text"
        assert isinstance(node.children, list)
        assert len(node.children) == 1
        assert node.children[0].tag == "span"
        assert node.props["href"] == "https://example.com"

    def test_HTMLNODE_initialization_with_defaults(self):
        node = HTMLNODE()
        assert node.tag is None
        assert node.value is None
        assert node.children is None
        assert node.props is None

    def test_HTMLNODE_repr(self):
        node = HTMLNODE("a", "this is an example text", None, {"href": "https://www.google.com", "target": "_blank"})
        assert repr(node) == "HTMLNODE(a, this is an example text, None, href: https://www.google.com, target: _blank)"

    # Test LeafNode

    def test_LeafNode_eq(self):
        node = LeafNode("p", "this is an example text", None)
        node2 = LeafNode("p", "this is an example text", None)
        self.assertEqual(node, node2)

    def test_LeafNode_repr_prop(self):
        node = LeafNode("p", "this is an example text", {"href": "https://www.google.com", "target": "_blank"})
        assert repr(node) == "LeafNode(p, this is an example text, href: https://www.google.com, target: _blank)"

    def test_LeafNode_repr_noprop(self):
        node = LeafNode("a", "example link!")
        assert repr(node) == "LeafNode(a, example link!, None)"

    def test_LeafNode_to_html_text(self):
        node = LeafNode("b", "example text").to_html()
        assert node == "<b>example text</b>"
        
    def test_LeafNode_to_html_a(self):
        node = LeafNode("a", "example text", {"href": "https://www.example.com"})
        result = node.to_html()
        assert result == '<a href="https://www.example.com">example text</a>'


    # Test ParentNode

    def test_ParentNode_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
                )
        result = node.to_html()
        assert result == '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'

    
    def test_ParentNode_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
                )
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
                )
        self.assertEqual(node, node2)


    def test_ParentNode_repr(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
                )
        assert repr(node) == "ParentNode(p, [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], None)"



if __name__ == "__main__":
    unittest.main()
