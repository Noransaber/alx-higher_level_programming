#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    list_of_items = []
    for item in sys.argv[1:]:
        list_of_items.append(item)

    save_to_json_file(list_of_items, "add_item.json")


if __name__ == "__main__":
    main()
