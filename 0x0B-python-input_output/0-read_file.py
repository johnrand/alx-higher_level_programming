#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read.
        Defaults to an empty string.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """

    if filename:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    else:
        print("No filename provided.")
