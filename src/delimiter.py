from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    delimiter_trigger = False

    delimiter_to_texttype = {
    '`': TextType.CODE,
    '**': TextType.BOLD,
    '*': TextType.ITALIC
    }

    for node in old_nodes:
        if text_type != TextType.NORMAL:
            new_nodes.append(node)
        node_text = node.text
        split_text = node_text.split(delimiter)
        for text in split_text:
            if delimiter_trigger == False:
                new_nodes.append(TextNode(text, TextType.NORMAL))
                delimiter_trigger = True
            else:
                text_type = delimiter_to_texttype.get(delimiter, TextType.NORMAL)
                new_nodes.append(TextNode(text, text_type))
                delimiter_trigger = False
    if delimiter_trigger == True:
        raise Exception("incomplete delimiter sequence")

    return new_nodes       
