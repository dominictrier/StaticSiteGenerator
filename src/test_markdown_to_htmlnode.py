import unittest
from markdown_to_htmlnode import markdown_to_html_node
from htmlnode import ParentNode


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

* This is the first *list* item in a list block
* This is a **list** item
* This is another list item

1. list *one*
2. list **two**
3. list three"""

        
        expected = ParentNode(
            'div',
            [
                '<h3>This is a <b>cool</b> heading</h3>',
                '<p><li>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</li><li>This is a second line o paragraph code with <b>bold</b> test.</li></p>',
                '<p><li>This is a new paragraph line</li></p>',
                '<pre><code>this is some cool code</code></pre>',
                '<blockquote><p>quote line 1 with <i>italic</i> text</p><p>quote line 2 with <b>bold</b> text</p><p>quote line 3</p></blockquote>',
                '<ul><li>This is the first <i>list</i> item in a list block</li><li>This is a <b>list</b> item</li><li>This is another list item</li></ul>',
                '<ul><li>This is the first <i>list</i> item in a list block</li><li>This is a <b>list</b> item</li><li>This is another list item</li></ul>',
                '<ol><li>list <i>one</i></li><li>list <b>two</b></li><li>list three</li></ol>'
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
