

def markdown_to_blocks(markdown):
    new_list = []
    lines_list = markdown.split("\n")
    for item in lines_list:
        if len(item) > 0:
            new_list.append(item.strip())

    return new_list
