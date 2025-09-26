# -*- coding: utf-8 -*-
"""Penney main."""
import sys
from penney.functions import print_description, menu_handler


def main():
    """
    CLI main function.

    :return: None
    """
    args = sys.argv
    print_description()
    if len(args) < 2:
        while (True):
            menu_handler()
            control_input = input(
                "\nPress [R] to restart or any other key to exit.")
            if control_input.upper() != "R":
                break


if __name__ == "__main__":
    main()
