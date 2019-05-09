def navlink(hlevel, htext, fragid):
    """
    Compose markdown link at the correct indentation for heading.

    # TODO used to be named construct_nav_link
    """
    # Set the indentation based on heading level
    markdown_link = ' ' * (hlevel - 1)
    # Add anchor text
    markdown_link += '- [' + htext[hlevel:].strip() + ']'
    # Set "name" value as href for this anchor
    markdown_link += '(#' + fragid + ')\n'
    return markdown_link


def anchorlink(fragid):
    return '<a name="' + fragid + '"></a>\n'
