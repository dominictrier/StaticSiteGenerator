from markdown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_blocktype
from htmlnode import LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    htmlnodes = []
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_blocktype(block)
        if block_type == "heading":
            result = header_to_html(block)
            htmlnodes.append(result)
        elif block_type == "code":
            result = code_to_html(block)
            htmlnodes.append(result)
        elif block_type == "quote":
            result = quote_to_html(block)
            htmlnodes.append(result)
        elif block_type == "unordered list":
            result = ul_list_to_html(block)
            htmlnodes.append(result)
        elif block_type == "ordered list":
            result = ol_list_to_html(block)
            htmlnodes.append(result)
        elif block_type == "paragraph":
            result = paragraph_to_html(block)
            htmlnodes.append(result)
    return ParentNode("div", htmlnodes)



def header_to_html(markdown):
    text = markdown.split(" ", 1)
    amount = text[0].count("#")
    children = text_to_children(text[1])
    node = ParentNode(f'h{amount}', children)
    node_html = node
    return node_html


def code_to_html(markdown):
    text = markdown.split("```")
    value = text[1]
    node_text = LeafNode(None, value)
    node_pre = ParentNode("code", [node_text])
    node_code = ParentNode('pre', [node_pre])
    return node_code


def quote_to_html(markdown):
    children = []
    for line in markdown.splitlines():
        text_body = line.split(" ", 1)[1]
        nodes = text_to_children(text_body)
        children.append(ParentNode("p", nodes))
    return ParentNode("blockquote", children)


def ul_list_to_html(markdown):
    children = []
    for line in markdown.splitlines():
        text_body = line.split(" ", 1)[1]
        nodes = text_to_children(text_body)
        children.append(ParentNode("li", nodes))
    return ParentNode("ul", children)


def ol_list_to_html(markdown):
    children = []
    for line in markdown.splitlines():
        text_body = line.split(" ", 1)[1]
        nodes = text_to_children(text_body)
        children.append(ParentNode("li", nodes))
    return ParentNode("ol", children)


# def paragraph_to_html(markdown):
#     children = []
#     lines = markdown.splitlines()

#     for i, line in enumerate(lines):
#         nodes = text_to_children(line)
#         if nodes and i < len(lines) -1:
#             last_node = nodes[-1]
#             new_node = LeafNode(last_node.tag, last_node.value + "<br>")
#             nodes[-1] = new_node
#         children.extend(nodes)

#     return ParentNode("p", children)


def paragraph_to_html(markdown):
    children = []
    lines = markdown.splitlines()

    for i, line in enumerate(lines):
        nodes = text_to_children(line)
        children.extend(nodes)
        if i < len(lines) - 1:
            children.append(LeafNode(None, "<br>"))

    return ParentNode("p", children)



def text_to_children(markdown):
    text_nodes = text_to_textnodes(markdown)
    processed_nodes = [node.textnode_to_htmlnode() for node in text_nodes]
    return processed_nodes