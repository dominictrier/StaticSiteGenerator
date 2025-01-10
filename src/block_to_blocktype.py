import re


def block_to_blocktype(markdown):
    if re.fullmatch(r"^#{1,6} .*", markdown, re.DOTALL):
        return "heading"
    if re.fullmatch(r"^``` .* ```$", markdown.strip(), re.DOTALL):
        return "code"
    if re.fullmatch(r"^> .*", markdown.strip(), re.DOTALL):
        return "quote"
    if all(re.match(r"^[*-]", line.strip()) for line in markdown.splitlines()):
        return "unordered list"
    lines = markdown.splitlines()
    if all(re.match(rf"^{i}\. ", line.strip()) for i, line in enumerate(lines, start=1)):
        return "ordered list"

    return "paragraph"
