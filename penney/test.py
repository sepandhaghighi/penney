# -*- coding: utf-8 -*-
"""
>>> from penney.function import *
>>> import random
>>> line(10,"*")
**********
>>> line()
###########
>>> print("\n".join(justify(["word1","word2","word3"],100)))
word1 word2 word3
>>> random.seed(2)
>>> seq_generator()
'T'
>>> random.seed(5)
>>> seq_generator()
'H'
>>> find_winner("HTTTHH",{"Player1":"HTT","Player2":"TTH"})
'Player1'
>>> find_winner("TTTTTTT",{"Player1":"HTT","Player2":"TTH"})
>>> find_winner("TTTTTTTH",{"Player1":"HTT","Player2":"TTH"})
'Player2'
>>> random.seed(246)
>>> game({"Player1":"HTT","Player2":"TTH"},iter=1)
{'Player1': 1, 'Player2': 0}
>>> random.seed(250)
>>> game({"Player1":"HTT","Player2":"TTH"},iter=1,print_status=True)
Round 1
HHTT
Point for -->Player1
###########
{'Player1': 1, 'Player2': 0}
>>> random.seed(260)
>>> game({"Player1":"HTT","Player2":"TTH"},iter=3,print_status=True)
Round 1
TTH
Point for -->Player2
###########
Round 2
HTT
Point for -->Player1
###########
Round 3
HHTHTT
Point for -->Player1
###########
{'Player1': 2, 'Player2': 1}
>>> check_seq(seq="HTHH",seq_len=4,seq_dict={1:"HTTT",2:"HHHH"})
True
>>> check_seq(seq="HTHH",seq_len=3,seq_dict={1:"HTTT",2:"HHHH"})
False
>>> check_seq(seq="HTHA",seq_len=4,seq_dict={1:"HTTT",2:"HHHH"})
False
>>> check_seq(seq="HHHH",seq_len=4,seq_dict={1:"HTTT",2:"HHHH"})
False
"""
