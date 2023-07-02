#!/usr/bin/python3
""" Define the function """


def text_indentation(text):
    """ print test with two new line if the ., ?, : exist

    args:
        text
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    output = ""
    i = 0
    while i < len(text) and text[i] == '':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
