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
>>> check_name("Name1",["Name2"])
True
>>> check_name("Name1",["Name1","Name2"])
False
>>> print_result(scores={"Player1":30,"Player2":32},seq_dict={"Player1":"HHT","Player2":"HTH"})
Scores Table :
Player2     32     HTH
Player1     30     HHT
Winner : Player2
>>> random.seed(300)
>>> computer_seq("HTH")
'HHT'
>>> player_filter(num=1,seq_len=3,print_status=True)
[Warning] Number of players automatically set to 2
2
>>> player_filter(num=3,seq_len=3,print_status=True)
3
>>> player_filter(num=9,seq_len=3,print_status=True)
[Warning] Number of players automatically set to 8
8
>>> description()
 ____                                                             ____
/\  _`\                                                          /\  _`\
\ \ \L\ \   __     ___      ___       __    __  __               \ \ \L\_\     __       ___ ___       __
 \ \ ,__/ /'__`\ /' _ `\  /' _ `\   /'__`\ /\ \/\ \               \ \ \L_L   /'__`\   /' __` __`\   /'__`\
  \ \ \/ /\  __/ /\ \/\ \ /\ \/\ \ /\  __/ \ \ \_\ \               \ \ \/, \/\ \L\.\_ /\ \/\ \/\ \ /\  __/
   \ \_\ \ \____\\ \_\ \_\\ \_\ \_\\ \____\ \/`____ \               \ \____/\ \__/.\_\\ \_\ \_\ \_\\ \____\
    \/_/  \/____/ \/_/\/_/ \/_/\/_/ \/____/  `/___/> \               \/___/  \/__/\/_/ \/_/\/_/\/_/ \/____/
                                                /\___/
                                                \/__/
<BLANKLINE>
          ___      _
__   __  / _ \    / |
\ \ / / | | | |   | |
 \ V /  | |_| | _ | |
  \_/    \___/ (_)|_|
<BLANKLINE>
<BLANKLINE>
####################################################################################################
Penney's  game,  named after its inventor Walter Penney, is a binary (head/tail) sequence generating
game  between  two  or  more players. Player A selects a sequence of heads and tails (of length 3 or
larger),  and  shows  this sequence to player B. Player B then selects another sequence of heads and
tails  of the same length. Subsequently, a fair coin is tossed until either player A's or player B's
sequence  appears  as a consecutive subsequence of the coin toss outcomes. The player whose sequence
appears first wins.
####################################################################################################
 __  __  _____  _   _  _   _
|  \/  || ____|| \ | || | | |  _
| |\/| ||  _|  |  \| || | | | (_)
| |  | || |___ | |\  || |_| |  _
|_|  |_||_____||_| \_| \___/  (_)
<BLANKLINE>
<BLANKLINE>
"""
