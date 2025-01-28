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
        if block_type == "code":
            result = code_to_html(block)
            htmlnodes.append(result)
        if block_type == "quote":
            result = quote_to_html(block)
            htmlnodes.append(result)
        if block_type == "unordered list":
            result = ul_list_to_html(block)
            htmlnodes.append(result)
        if block_type == "ordered list":
            result = ol_list_to_html(block)
            htmlnodes.append(result)
        if block_type == "paragraph":
            result = paragraph_to_html(block)
            htmlnodes.append(result)
    return ParentNode("div", htmlnodes)


def header_to_html(markdown):
    text = markdown.split(" ", 1)
    amount = text[0].count("#")
    children = text_to_children(text[1])
    node = ParentNode(f'h{amount}', children)
    node_html = node#.to_html()
    return node_html


def code_to_html(markdown):
    text = markdown.split("```")
    value = text[1]
    node_code = LeafNode("code", value)#.to_html()
    node_pre = LeafNode('pre', node_code)#.to_html()
    return node_pre


def quote_to_html(markdown):
    children = []
    for line in markdown.splitlines():
        text_body = line.split(" ", 1)[1]
        nodes = text_to_children(text_body)
        children.append(ParentNode("p", nodes))
    return ParentNode("blockquote", children)#.to_html()


def ul_list_to_html(markdown):
    children = []
    for line in markdown.splitlines():
        text_body = line.split(" ", 1)[1]
        nodes = text_to_children(text_body)
        children.append(ParentNode("li", nodes))
    return ParentNode("ul", children)#.to_html()


def ol_list_to_html(markdown):
    children = []
    for line in markdown.splitlines():
        text_body = line.split(" ", 1)[1]
        nodes = text_to_children(text_body)
        children.append(ParentNode("li", nodes))
    return ParentNode("ol", children)#.to_html()


def paragraph_to_html(markdown):
    children = []
    lines = markdown.splitlines()
    for i, line in enumerate(lines):
        nodes = text_to_children(line)
        children.extend(nodes)
        if i < len(lines) - 1:
            children.append(LeafNode(None, "<br>"))
    return ParentNode("p", children)#.to_html()


def text_to_children(markdown):
    text_nodes = text_to_textnodes(markdown)
    processed_nodes = [node.textnode_to_htmlnode() for node in text_nodes]
    return processed_nodes
