from markdown_extractor import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        try:
            original_text = node.text
            extracted_images = extract_markdown_images(original_text)
            working_text = original_text
            
            for item in extracted_images:
                image_alt = item[0]
                image_link = item[1]
                sections = working_text.split(f"![{image_alt}]({image_link})", 1)
                if len(sections[0]) > 0:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                working_text = sections[1]
            if len(working_text) > 0:
                new_nodes.append(TextNode(working_text, TextType.NORMAL))

        except ValueError:
            if len(node.text) > 0:
                new_nodes.append(node)

    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        try:
            original_text = node.text
            extracted_links = extract_markdown_links(original_text)
            working_text = original_text
            
            for item in extracted_links:
                link_alt = item[0]
                link_url = item[1]
                sections = working_text.split(f"[{link_alt}]({link_url})", 1)
                if len(sections[0]) > 0:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
                working_text = sections[1]
            if len(working_text) > 0:
                new_nodes.append(TextNode(working_text, TextType.NORMAL))

        except ValueError:
            if len(node.text) > 0:
                new_nodes.append(node)

    return new_nodes
