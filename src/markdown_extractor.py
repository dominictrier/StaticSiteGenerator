import re


def extract_markdown_images(text: str):
    results = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    if results:
        return results
    else:
        raise ValueError("no images found")


def extract_markdown_links(text: str):
    results = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    if results:
        return results
    else:
        raise ValueError("no links found")

