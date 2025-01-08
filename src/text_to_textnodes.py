from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
from split_nodes import split_nodes_images, split_nodes_links


def text_to_textnodes(text):
    new_node = TextNode(text, TextType.NORMAL)
    split_images = split_nodes_images([new_node])
    split_links = split_nodes_links(split_images)
    delimiter_code = split_nodes_delimiter(split_links, '`', TextType.CODE)
    delimiter_bold = split_nodes_delimiter(delimiter_code, '**', TextType.BOLD)
    delimiter_italic = split_nodes_delimiter(delimiter_bold, '*', TextType.ITALIC)

    return delimiter_italic
