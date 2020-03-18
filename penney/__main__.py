# -*- coding: utf-8 -*-
""""""
from penney.functions import *

if __name__ == "__main__":
    while(True):
        description()
        menu()
        control_input = input("Press [R] to restart or any other key to exit.")
        if control_input.upper() != "R":
            break
