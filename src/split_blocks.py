def markdown_to_blocks(markdown):
    return list(map(lambda x: x.strip(), markdown.split("\n\n")))