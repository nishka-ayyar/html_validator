#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html
    validation by checking whether every opening tag
    has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    stack = []
    justags = _extract_tags(html)
    # print(justags)
    for tag in justags:
        if "/" not in tag:
            stack.append(tag)
        else:
            if len(stack) == 0:
                return False
            if "/" not in stack[-1] and "/" in tag and \
                    stack[-1][1:-1] == tag[2:-1]:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

    # HINT:
    # use the _extract_tags function below to generate
    # a list of html tags without any extra text;
    # then process these html tags using the
    # balanced parentheses algorithm from the class/book
    # the main difference between your code and the code from class
    # will be that you will have to keep track of not just the 3 types
    # of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are
    not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained
    in the input string,
    stripping out all the text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    i = 0
    tags = []
    while i < len(html):
        # print(i)
        if html[i] == "<":
            for j in range(i, len(html)):
                if html[j] == ">":
                    tags.append(html[i:j + 1])
                    i = j + 1
                    break
                if j == len(html) - 1:
                    tags.append(html[i:])
                    return tags
        else:
            i += 1
    return tags
