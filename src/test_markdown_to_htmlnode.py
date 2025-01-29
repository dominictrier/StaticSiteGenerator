import unittest
from markdown_to_htmlnode import markdown_to_html_node
from htmlnode import ParentNode, LeafNode


class TestTextToTextNodes(unittest.TestCase):


    def test_complex_string_assert(self):
        test_string = """### This is a **cool** heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.
This is a second line o paragraph code with **bold** test.

This is a new paragraph line

```this is some cool code```

> quote line 1 with *italic* text
> quote line 2 with **bold** text
> quote line 3

- This is the first *list* item in a list block
- This is a **list** item
- This is another list item

* First item with a *different* style
* Another **unique** item here
* Third distinct item

1. list *one*
2. list **two**
3. list three"""

        
        expected = ParentNode(
    "div", [
        ParentNode("h3", [
            LeafNode(None, "This is a "),
            LeafNode("b", "cool"),
            LeafNode(None, " heading")
        ]),
        ParentNode("p", [
            LeafNode(None, "This is a paragraph of text. It has some "),
            LeafNode("b", "bold"),
            LeafNode(None, " and "),
            LeafNode("i", "italic"),
            LeafNode(None, " words inside of it."),
            LeafNode(None, "<br>"),
            LeafNode(None, "This is a second line o paragraph code with "),
            LeafNode("b", "bold"),
            LeafNode(None, " test.")
        ]),
        ParentNode("p", [
            LeafNode(None, "This is a new paragraph line")
        ]),
        ParentNode("pre", [
            ParentNode("code", [
                LeafNode(None, "this is some cool code")
            ])
        ]),
        ParentNode("blockquote", [
            ParentNode("p", [
                LeafNode(None, "quote line 1 with "),
                LeafNode("i", "italic"),
                LeafNode(None, " text")
            ]),
            ParentNode("p", [
                LeafNode(None, "quote line 2 with "),
                LeafNode("b", "bold"),
                LeafNode(None, " text")
            ]),
            ParentNode("p", [
                LeafNode(None, "quote line 3")
            ])
        ]),
        ParentNode("ul", [
            ParentNode("li", [
                LeafNode(None, "This is the first "),
                LeafNode("i", "list"),
                LeafNode(None, " item in a list block")
            ]),
            ParentNode("li", [
                LeafNode(None, "This is a "),
                LeafNode("b", "list"),
                LeafNode(None, " item")
            ]),
            ParentNode("li", [
                LeafNode(None, "This is another list item")
            ])
        ]),
        ParentNode("ul", [
            ParentNode("li", [
                LeafNode(None, "First item with a "),
                LeafNode("i", "different"),
                LeafNode(None, " style")
            ]),
            ParentNode("li", [
                LeafNode(None, "Another "),
                LeafNode("b", "unique"),
                LeafNode(None, " item here")
            ]),
            ParentNode("li", [
                LeafNode(None, "Third distinct item")
            ])
        ]),
        ParentNode("ol", [
            ParentNode("li", [
                LeafNode(None, "list "),
                LeafNode("i", "one")
            ]),
            ParentNode("li", [
                LeafNode(None, "list "),
                LeafNode("b", "two")
            ]),
            ParentNode("li", [
                LeafNode(None, "list three")
            ])
        ])
    ]
)
        
        result = markdown_to_html_node(test_string)

        self.assertEqual(result, expected, "Test failed: test_complex_string_assert")


    def test_with_incomplete_markup_sequence(self):
        test_string = """This is a paragraph of text. It has some **bold* and *italic* words inside of it."""

        with self.assertRaisesRegex(Exception, r"Incomplete delimiter sequence"):
            markdown_to_html_node(test_string)


if __name__ == "__main__":
    unittest.main()
