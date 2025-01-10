import unittest
from block_to_blocktype import block_to_blocktype


class TestTextToTextNodes(unittest.TestCase):

    # positive tests

    def test_heading(self):
        test_string = "### this is a heading"
        result = block_to_blocktype(test_string)
        expected = "heading"
        
        self.assertEqual(result, expected,"Test failed: test_heading")


    def test_code_1line(self):
        test_string = "```this is a very cool code string```"
        result = block_to_blocktype(test_string)
        expected = "code"
        
        self.assertEqual(result, expected,"Test failed: test_code_1line")

    
    def test_code_3line(self):
        test_string =   """```this is a very
                        cool code string
                        that has multiple lines```"""
        result = block_to_blocktype(test_string)
        expected = "code"
        
        self.assertEqual(result, expected,"Test failed: test_code_3line")

    
    def test_blockquote_1line(self):
        test_string = "> this is a quote"
        result = block_to_blocktype(test_string)
        expected = "quote"
        
        self.assertEqual(result, expected,"Test failed: test_quote_1line")


    def test_quote_3line(self):
        test_string =   "> this is a very \
                        > cool quote string \
                        > that has multiple lines"
        result = block_to_blocktype(test_string)
        expected = "quote"
        
        self.assertEqual(result, expected,"Test failed: test_quote_3line")


    def test_unordered_list_stars(self):
        test_string =   "* list item 1 \
                        * list item 2 \
                        * list item 3"
        result = block_to_blocktype(test_string)
        expected = "unordered list"
        
        self.assertEqual(result, expected,"Test failed: test_unordered_list_stars")


    def test_unordered_list_dashes(self):
        test_string =   "- list item 1 \
                        - list item 2 \
                        - list item 3"
        result = block_to_blocktype(test_string)
        expected = "unordered list"
        
        self.assertEqual(result, expected,"Test failed: test_unordered_list_dashes")


    def test_ordered_list(self):
        test_string =   "1. list item 1 \
                        2. list item 2 \
                        3. list item 3"
        result = block_to_blocktype(test_string)
        expected = "ordered list"
        
        self.assertEqual(result, expected,"Test failed: test_ordered_list")


    def test_paragraph(self):
        test_string = "this is just a normal paragraph"
        result = block_to_blocktype(test_string)
        expected = "paragraph"
        
        self.assertEqual(result, expected,"Test failed: test_paragraph")


    # negative tests

    def test_ordered_list_wrong(self):
        test_string =   """1. list item 1
                        3. list item 2
                        6. list item 3"""
        result = block_to_blocktype(test_string)
        expected = "paragraph"
        
        self.assertEqual(result, expected,"Test failed: test_ordered_list_wrong")


if __name__ == "__main__":
    unittest.main()