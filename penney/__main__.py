# -*- coding: utf-8 -*-
"""Penney main."""
import sys
from penney.functions import *


def main():
    """
    CLI main function.

    :return: None
    """
    args = sys.argv
    description()
    if len(args) < 2:
        while (True):
            menu()
            control_input = input(
                "\nPress [R] to restart or any other key to exit.")
            if control_input.upper() != "R":
                break


if __name__ == "__main__":
    main()
