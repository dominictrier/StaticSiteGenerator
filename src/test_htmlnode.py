import unittest

from htmlnode import HTMLNODE

# print("HTMLNODE imported successfully!")


class TestHTMLNODE(unittest.TestCase): #node = HTMLNODE("a", "this is an example text", None, {"href": "https://www.google.com", "target": "_blank"})
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


if __name__ == "__main__":
    unittest.main()
