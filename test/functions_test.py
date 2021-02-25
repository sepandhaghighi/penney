# -*- coding: utf-8 -*-
"""
>>> from penney.functions import *
>>> import random
>>> line(10,"*")
**********
>>> line()
###########
>>> words = ["Word{}".format(str(i)) for i in range(40)]
>>> output = " ".join(justify(words,100))
>>> print(output)
Word0  Word1  Word2  Word3  Word4  Word5  Word6 Word7 Word8 Word9 Word10 Word11 Word12 Word13 Word14 Word15  Word16  Word17  Word18 Word19 Word20 Word21 Word22 Word23 Word24 Word25 Word26 Word27 Word28 Word29 Word30 Word31 Word32 Word33 Word34 Word35 Word36 Word37 Word38 Word39
>>> output = " ".join(justify(words,2))
>>> print(output)
Word0 Word1 Word2 Word3 Word4 Word5 Word6 Word7 Word8 Word9 Word10 Word11 Word12 Word13 Word14 Word15 Word16 Word17 Word18 Word19 Word20 Word21 Word22 Word23 Word24 Word25 Word26 Word27 Word28 Word29 Word30 Word31 Word32 Word33 Word34 Word35 Word36 Word37 Word38 Word39
>>> det([[1,0],[0,1]])
1.0
>>> det([[1,1],[1,1]])
0.0
>>> det([[2,1],[2,2]])
2.0
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
>>> result = game({"Player1":"HTT","Player2":"TTH"},round_number=1)
>>> result['Player1']
1
>>> result['Player2']
0
>>> random.seed(250)
>>> result = game({"Player1":"HTT","Player2":"TTH"},round_number=1,print_status=True)
Round 1
HHTT
Point for --> Player1
###########
>>> result['Player1']
1
>>> result['Player2']
0
>>> random.seed(260)
>>> result = game({"Player1":"HTT","Player2":"TTH"},round_number=3,print_status=True)
Round 1
TTH
Point for --> Player2
###########
Round 2
HTT
Point for --> Player1
###########
Round 3
HHTHTT
Point for --> Player1
###########
>>> result['Player1']
2
>>> result['Player2']
1
>>> check_seq(seq="HTHH",seq_len=4,seq_dict={1:"HTTT",2:"HHHH"})
True
>>> check_seq(seq="HTHH",seq_len=3,seq_dict={1:"HTTT",2:"HHHH"})
False
>>> check_seq(seq="HTHA",seq_len=4,seq_dict={1:"HTTT",2:"HHHH"})
False
>>> check_seq(seq="HHHH",seq_len=4,seq_dict={1:"HTTT",2:"HHHH"})
False
>>> check_name("Name1",["Name2"])
True
>>> check_name("Name1",["Name1","Name2"])
False
>>> print_seq("HTHHHT")
HTHHHT
>>> print_result(scores={"Player1":30,"Player2":32},seq_dict={"Player1":"HHT","Player2":"HTH"})
Scores Table :
Player2     32   HTH
Player1     30   HHT
Winner : Player2
>>> print_result(scores={"Player1":30,"Player2":30},seq_dict={"Player1":"HHT","Player2":"HTH"})
Scores Table :
Player2     30   HTH
Player1     30   HHT
Tie!
>>> random.seed(300)
>>> computer_seq_gen(3,"HTH")
'HHT'
>>> random.seed(301)
>>> computer_seq_gen(3)
'HHH'
>>> player_filter(num=1,seq_len=3,print_status=True)
[Warning] Number of players automatically set to 2
2
>>> player_filter(num=3,seq_len=3,print_status=True)
3
>>> player_filter(num=9,seq_len=3,print_status=True)
[Warning] Number of players automatically set to 8
8
>>> print_prob(prob_calc({'A1':'THH', 'A2':'HTH', 'A3':'HHT'}))
Wining Probability : 
A1     41.667%
A2     33.333%
A3     25.000%
Winner should be A1
>>> print_prob(prob_calc({"2":"HTT","1":"HHH"}))
Wining Probability :
2     60.000%
1     40.000%
Winner should be 2
>>> print_prob(prob_calc({"2":"HHT","1":"TTT"}))
Wining Probability :
2     70.000%
1     30.000%
Winner should be 2
>>> print_prob(prob_calc({"1":"HHT","2":"TTT"}))
Wining Probability :
1     70.000%
2     30.000%
Winner should be 1
"""
