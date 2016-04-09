def shrink_content(content):

    if len(content) > 200:
        return content[:200]
    else:
        return content
