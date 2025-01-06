import unittest
from markdown_extractor import extract_markdown_images, extract_markdown_links


class TestSplitNodesDelimiter(unittest.TestCase):

    # Test Images

    def test_simple_img(self):
        sample = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        result = extract_markdown_images(sample)

        expected = [
            ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'),
            ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')
            ]
        
        self.assertEqual(result,expected, "Test failed: test_simple_img")


    def test_no_img_provided(self):
        sample = "This is a sample text without image"

        with self.assertRaisesRegex(ValueError, r"no images found"):
            extract_markdown_images(sample)

    # Test Links

    def test_simple_link(self):
        sample = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        result = extract_markdown_links(sample)

        expected = [
            ('to boot dev', 'https://www.boot.dev'),
            ('to youtube', 'https://www.youtube.com/@bootdotdev')
            ]
        
        self.assertEqual(result, expected, "Test failed: test_simple_link")


    def test_no_link_provided(self):
        sample = "This is a sample text without link"

        with self.assertRaisesRegex(ValueError, r"no links found"):
            extract_markdown_links(sample)


if __name__ == "__main__":
    unittest.main()
