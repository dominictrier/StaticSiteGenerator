

# def markdown_to_blocks(markdown):
#     new_list = []
#     lines_list = markdown.split("\n\n")
#     for item in lines_list:
#         if len(item) > 0:
#             new_list.append(item.strip())

#     return new_list


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
