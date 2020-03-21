# -*- coding: utf-8 -*-
"""Penney main."""
from penney.functions import *

if __name__ == "__main__":
    while(True):
        description()
        menu()
        control_input = input(
            "\nPress [R] to restart or any other key to exit.")
        if control_input.upper() != "R":
            break
