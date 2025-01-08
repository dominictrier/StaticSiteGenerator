from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
from markdown_extractor import extract_markdown_images, extract_markdown_links
from split_nodes import split_nodes_images, split_nodes_links

def text_to_textnodes(text):
    
    new_node = TextNode(text, TextType.NORMAL)
    split_images = split_nodes_images([new_node])
    split_links = split_nodes_links(split_images)
    delimiter_code = split_nodes_delimiter(split_links, '`', TextType.CODE)
    delimiter_bold = split_nodes_delimiter(delimiter_code, '**', TextType.BOLD)
    delimiter_italic = split_nodes_delimiter(delimiter_bold, '*', TextType.ITALIC)

    print(delimiter_italic)






test_string = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
result = text_to_textnodes(test_string)
print(result)