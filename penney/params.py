# -*- coding: utf-8 -*-
"""Penney params."""

PENNEY_VERSION = "0.1"

PENNEY_DESCRIPTION = """
Penney's game, named after its inventor Walter Penney, is a binary (head/tail) sequence generating game between two or more players.
Player A selects a sequence of heads and tails (of length 3 or larger), and shows this sequence to player B. Player B then selects
another sequence of heads and tails of the same length. Subsequently, a fair coin is tossed until either player A's or player B's sequence
appears as a consecutive subsequence of the coin toss outcomes. The player whose sequence appears first wins.
"""

TRY_MESSAGE = "Try again!"

PLAYER_COMPUTER_MESSAGE = "Play with computer [1]\nPlay with other players [any other key]\nPlease select : "

ROUND_NUMBER_MESSAGE = "Please enter number of rounds : "

ROUND_NUMBER_ERROR = "[Error] Number of rounds should be an integer\n" + TRY_MESSAGE

PLAYER_NUMBER_MESSAGE = "Please enter number of players : "

PLAYER_NUMBER_ERROR = "[Error] Number of players should be an integer\n" + TRY_MESSAGE

PLAYER_NUMBER_WARNING = "[Warning] Number of players automatically set to {}"

PLAYER_NAME_MESSAGE = "Please enter player-{} name : "

PLAYER_NAME_ERROR = "[Error] Player name should be uniqe and contains at least one character" + TRY_MESSAGE

LENGTH_MESSAGE = "Please enter sequence length : "

LENGTH_ERROR1 = "[Error] Sequence length should be greater than 2\n" + TRY_MESSAGE

LENGTH_ERROR2 = "[Error] Sequence length should be an integer\n" + TRY_MESSAGE

SEQ_MESSAGE = "[{}] Please enter your sequence : "

SEQ_ERROR = "[Error] Sequence should be uniqe, only consist of 'T' and 'H' characters with length of {}"

COMPUTER_SEQ_MESSAGE = "{0} sequence : {1}"

POINT_MESSAGE = "Point for --> {}"
