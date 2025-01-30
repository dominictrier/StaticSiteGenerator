from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
            
        node_text = node.text
        split_text = node_text.split(delimiter)
        
        if len(split_text) % 2 == 0:
            raise Exception("Incomplete delimiter sequence")

        for i, text in enumerate(split_text):
            if not text:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.NORMAL))
            else:
                new_nodes.append(TextNode(text, text_type))


    return new_nodes      
