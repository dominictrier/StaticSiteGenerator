import unittest
from markdown_to_htmlnode import markdown_to_html_node
from htmlnode import ParentNode, LeafNode


class TestTextToTextNodes(unittest.TestCase):

    def test_complex_string(self):
        test_string = """### This is a **cool** heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

```this is some cool code```

> quote line 1 with *italic* text
> quote line 2 with **bold** text
> quote line 3

- This is the first *list* item in a list block
- This is a **list** item
- This is another list item

* This is the first *list* item in a list block
* This is a **list** item
* This is another list item

1. list *one*
2. list **two**
3. list three"""
        
        node = markdown_to_html_node(test_string)

        assert node.tag == "div"
        assert node.value == None
        assert len(node.children) == 1
        assert node.children[0].tag == "h3"
        assert node.props == None


if __name__ == "__main__":
    unittest.main()
