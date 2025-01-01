from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if text_type != TextType.NORMAL:
            new_nodes.append(node)
        
