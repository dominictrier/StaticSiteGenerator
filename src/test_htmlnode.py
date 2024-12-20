import unittest

from htmlnode import HTMLNODE, LeafNode

# print("HTMLNODE imported successfully!")


class TestHTMLNODE(unittest.TestCase): #node = HTMLNODE("a", "this is an example text", None, {"href": "https://www.google.com", "target": "_blank"})

    # Test HTMLNODE

    def test_eq(self):
        node = HTMLNODE("a", "this is an example text", None)
        node2 = HTMLNODE("a", "this is an example text", None)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = HTMLNODE("a", "this is an example text", None)
        node2 = HTMLNODE("b", "this is an example text", None)
        self.assertNotEqual(node, node2)

    def test_initialization_with_all_attributes(self):
        node = HTMLNODE("a", "link text", [HTMLNODE("span", "child")], {"href": "https://example.com"})
        assert node.tag == "a"
        assert node.value == "link text"
        assert isinstance(node.children, list)
        assert len(node.children) == 1
        assert node.children[0].tag == "span"
        assert node.props["href"] == "https://example.com"

    def test_initialization_with_defaults(self):
        node = HTMLNODE()
        assert node.tag is None
        assert node.value is None
        assert node.children is None
        assert node.props is None

    def test_repr(self):
        node = HTMLNODE("a", "this is an example text", None, {"href": "https://www.google.com", "target": "_blank"})
        assert repr(node) == "HTMLNODE(a, this is an example text, None, href: https://www.google.com, target: _blank)"

    # Test LeafNode

    def test_leafnode_eq(self):
        node = LeafNode("p", "this is an example text", None)
        node2 = LeafNode("p", "this is an example text", None)
        self.assertEqual(node, node2)

    def test_leafnode_repr_prop(self):
        node = LeafNode("p", "this is an example text", {"href": "https://www.google.com", "target": "_blank"})
        assert repr(node) == "LeafNode(p, this is an example text, href: https://www.google.com, target: _blank)"

    def test_leafnode_repr_noprop(self):
        node = LeafNode("a", "example link!")
        assert repr(node) == "LeafNode(a, example link!, None)"

    def test_leafnode_to_html_text(self):
        node = LeafNode("b", "example text").to_html()
        assert node == "<b>example text</b>"
        
    def test_leafnode_to_html_a(self):
        node = LeafNode("a", "example text", {"href": "https://www.example.com"})
        result = node.to_html()
        assert result == '<a href="https://www.example.com">example text</a>'

if __name__ == "__main__":
    unittest.main()
