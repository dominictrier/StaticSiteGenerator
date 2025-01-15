from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
from split_nodes import split_nodes_images, split_nodes_links


def text_to_textnodes(text):
    node = TextNode(text, TextType.NORMAL)
    node = split_nodes_images([node])
    node = split_nodes_links(node)
    node = split_nodes_delimiter(node, '`', TextType.CODE)
    node = split_nodes_delimiter(node, '**', TextType.BOLD)
    node = split_nodes_delimiter(node, '*', TextType.ITALIC)

    return node
