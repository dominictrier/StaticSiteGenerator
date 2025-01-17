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
        
        result = markdown_to_html_node(test_string)

        expected = ParentNode('div', ['<h3>This is a <b>cool</b> heading</h3>', '<pre><code>this is some cool code</code></pre>', '<blockquote><p>quote line 1 with <i>italic</i> text</p><p>quote line 2 with <b>bold</b> text</p><p>quote line 3</p></blockquote>', '<ul><li>This is the first <i>list</i> item in a list block</li><li>This is a <b>list</b> item</li><li>This is another list item</li></ul>', '<ul><li>This is the first <i>list</i> item in a list block</li><li>This is a <b>list</b> item</li><li>This is another list item</li></ul>', '<ol><li>list <i>one</i></li><li>list <b>two</b></li><li>list three</li></ol>'], None)
        
        self.assertEqual(result, expected,"Test failed: test_complex_string")


if __name__ == "__main__":
    unittest.main()
