#!/usr/bin/python3

"""Defining the Markdown to html converter function
"""


import sys
import os

def main():
    """
    Entry point for the script
    Defining the converter function
    """

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()