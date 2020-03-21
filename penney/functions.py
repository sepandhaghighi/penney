# -*- coding: utf-8 -*-
"""Penney functions."""
import random
import time
from .params import *
from art import tprint


def line(num=11, char="#"):
    """
    Print line of char.

    :param num: number of character in this line
    :type num : int
    :param char: character
    :type char : str
    :return: None
    """
    print(char * num)


def left_justify(words, width):
    """
    Left justify words.

    :param words: list of words
    :type words : list
    :param width: width of each line
    :type width: int
    :return: left justified words as list
    """
    return ' '.join(words).ljust(width)


def justify(words, width):
    """
    Justify input words.

    :param words: list of words
    :type words : list
    :param width: width of each line
    :type width : int
    :return: list of justified words as list
    """
    line = []
    col = 0
    for word in words:
        if line and col + len(word) > width:
            if len(line) == 1:
                yield left_justify(line, width)
            else:
                # After n + 1 spaces are placed between each pair of
                # words, there are r spaces left over; these result in
                # wider spaces at the left.
                n, r = divmod(width - col + 1, len(line) - 1)
                narrow = ' ' * (n + 1)
                if r == 0:
                    yield narrow.join(line)
                else:
                    wide = ' ' * (n + 2)
                    yield wide.join(line[:r] + [narrow.join(line[r:])])
            line, col = [], 0
        line.append(word)
        col += len(word) + 1
    if line:
        yield left_justify(line, width)


def seq_generator():
    """
    Generate each part of sequence.

    :return: sequence part as str
    """
    return random.choice(["T", "H"])


def find_winner(seq, seq_dict):
    """
    Identify each round winner.

    :param seq: round sequence
    :type seq: str
    :param seq_dict: players sequences
    :type seq_dict: dict
    :return: winner name as str
    """
    winner_name = ""
    min_index = len(seq)
    for name in seq_dict.keys():
        name_index = seq.find(seq_dict[name])
        if name_index != -1:
            if name_index < min_index:
                winner_name = name
                min_index = name_index
    if len(winner_name) != 0:
        return winner_name
    return None


def game(seq_dict, round_number=100, print_status=False):
    """
    Game simulation.

    :param seq_dict: players sequences
    :type seq_dict: dict
    :param round_number: number of rounds
    :type round_number: int
    :param print_status: print status flag
    :type print_status: bool
    :return: scores as dict
    """
    round_num = 0
    scores = {name: 0 for name in seq_dict.keys()}
    while(round_num < round_number):
        next_round = False
        round_seq = ""
        while(not next_round):
            round_seq += seq_generator()
            winner = find_winner(round_seq, seq_dict)
            if winner is not None:
                if print_status:
                    print("Round {}".format(str(round_num + 1)))
                    print(round_seq)
                    print(POINT_MESSAGE.format(winner))
                    line()
                    time.sleep(1)
                scores[winner] += 1
                next_round = True
        round_num += 1
    return scores


def check_seq(seq, seq_len, seq_dict):
    """
    Check the validity of sequence.

    :param seq: test sequence
    :type seq: str
    :param seq_len: sequence length
    :type seq_len: int
    :param seq_dict: players sequences
    :type seq_dict: dict
    :return: validity as bool
    """
    seq_elements = set(list(seq))
    if len(seq) == seq_len and seq_elements.issubset(
            {"T", "H"}) and seq not in seq_dict.values():
        return True
    return False


def get_seq(seq_len, names_dict, computer_seq=None):  # pragma: no cover
    """
    Get sequence from user.

    :param seq_len: sequence length
    :type seq_len: int
    :param names_dict: players names
    :type names_dict: dict
    :param computer_seq: computer sequence
    :type computer_seq: str
    :return: players sequences as dict
    """
    seq_dict = {name: "" for name in names_dict.values()}
    for player_ord in sorted(names_dict.keys()):
        while(True):
            player_name = names_dict[player_ord]
            seq_select = input(SEQ_MESSAGE.format(str(player_name)))
            if check_seq(
                    seq_select,
                    seq_len,
                    seq_dict) and seq_select != computer_seq:
                seq_dict[player_name] = seq_select
                break
            else:
                print(SEQ_ERROR.format(str(seq_len)))
    return seq_dict


def get_len():  # pragma: no cover
    """
    Get sequence length from user.

    :return: sequence length as int
    """
    seq_len = 0
    while(True):
        try:
            seq_len = int(input(LENGTH_MESSAGE))
            if seq_len >= 3:
                break
            else:
                print(LENGTH_ERROR1)
        except Exception:
            print(LENGTH_ERROR2)
    return seq_len


def check_name(name, name_list):
    """
    Check the validity of name.

    :param name: test name
    :type name: str
    :param name_list: players names
    :type name_list: list
    :return: validity as bool
    """
    if len(name) != 0 and name not in name_list:
        return True
    return False


def get_names(num=2):  # pragma: no cover
    """
    Get names from user.

    :param num: number of players
    :type num: int
    :return: players names as dict
    """
    names_dict = {}
    names_order = list(range(1, num + 1))
    index = 0
    while(index < num):
        while(True):
            name = input(PLAYER_NAME_MESSAGE.format(str(index + 1)))
            if check_name(name, names_dict):
                rand_order = random.choice(names_order)
                names_order.remove(rand_order)
                names_dict[rand_order] = name
                break
            else:
                print(PLAYER_NAME_ERROR)
        index += 1
    return names_dict


def print_result(scores, seq_dict):
    """
    Print game result.

    :param scores: players scores
    :type scores: dict
    :param seq_dict: players sequences
    :type seq_dict: dict
    :return: None
    """
    sorted_scores = sorted(
        scores.items(), key=lambda x: (
            x[1], x[0]), reverse=True)
    name_max_length = max(map(len, scores.keys()))
    score_max_length = max(map(lambda x: len(str(x)), scores.values()))
    print("Scores Table : ")
    for item in sorted_scores:
        score = item[1]
        name = item[0]
        space_name = (name_max_length - len(name) + 5) * " "
        space_score = (score_max_length - len(str(score)) + 3) * " "
        print(name + space_name + str(score) + space_score + seq_dict[name])
    if len(set(scores.values())) > 1:
        print("Winner : {}".format(sorted_scores[0][0]))
    else:
        print("Tie!")


def get_number(message, error_message):  # pragma: no cover
    """
    Get a number from user.

    :param message: user message
    :type message: str
    :param error_message: error message
    :type error_message: str
    :return: number as int
    """
    number = 0
    while(True):
        try:
            number = int(input(message))
            break
        except Exception:
            print(error_message)
    return number


def computer_seq_gen(seq_len, seq=None):
    """
    Generate computer sequence.

    :param seq_len: sequence length
    :type seq_len: int
    :param seq: player sequence
    :type seq: str
    :return: computer sequence as str
    """
    while(True):
        result = ""
        index = 0
        while(index < seq_len):
            result += seq_generator()
            index += 1
        if seq != result or seq is None:
            break
    return result


def player_filter(num, seq_len, print_status=False):
    """
    Filter number of players.

    :param num: number of players
    :type num: int
    :param seq_len: sequence length
    :type seq_len: int
    :param print_status: print status flag
    :type print_status: bool
    :return: filtered number of players as int
    """
    if num < 2:
        if print_status:
            print(PLAYER_NUMBER_WARNING.format("2"))
        return 2
    if num > 2**seq_len:
        if print_status:
            print(PLAYER_NUMBER_WARNING.format(str(2**seq_len)))
        return 2**seq_len
    return num


def computer_player_handler(seq_len):  # pragma: no cover
    """
    Computer-Player mode handler.

    :param seq_len: sequence length
    :type seq_len: int
    :return: players sequences as dict
    """
    names_dict = get_names(num=1)
    computer_name = "Computer"
    player_name = list(names_dict.values())[0]
    if player_name.upper() == 'COMPUTER':
        computer_name = "Bot"
    computer_seq = None
    first_coin = seq_generator()
    if first_coin == "T":
        computer_seq = computer_seq_gen(seq_len)
        print(COMPUTER_SEQ_MESSAGE.format(computer_name, computer_seq))
    seq_dict = get_seq(seq_len, names_dict, computer_seq)
    player_seq = list(seq_dict.values())[0]
    if computer_seq is None:
        computer_seq = computer_seq_gen(seq_len, player_seq)
        print(COMPUTER_SEQ_MESSAGE.format(computer_name, computer_seq))
    seq_dict[computer_name] = computer_seq
    return seq_dict


def player_player_handler(seq_len):  # pragma: no cover
    """
    Player-Player mode handler.

    :param seq_len: sequence length
    :type seq_len: int
    :return: players sequences as dict
    """
    player_number = get_number(PLAYER_NUMBER_MESSAGE, PLAYER_NUMBER_ERROR)
    player_number = player_filter(
        player_number,
        seq_len=seq_len,
        print_status=True)
    names_dict = get_names(num=player_number)
    seq_dict = get_seq(seq_len, names_dict)
    return seq_dict


def menu():  # pragma: no cover
    """
    CLI menu main handler.

    :return: None
    """
    player_or_computer = input(PLAYER_COMPUTER_MESSAGE)
    round_number = abs(get_number(ROUND_NUMBER_MESSAGE, ROUND_NUMBER_ERROR))
    seq_len = get_len()
    if player_or_computer != "1":
        seq_dict = player_player_handler(seq_len)
    else:
        seq_dict = computer_player_handler(seq_len)
    line()
    scores = game(seq_dict, round_number=round_number, print_status=True)
    print_result(scores, seq_dict)


def description():  # pragma: no cover
    """
    Print introduction and description.

    :return: None
    """
    tprint("Penney Game", font="larry3d")
    tprint("v {}".format(PENNEY_VERSION))
    line(100)
    print("\n".join(justify(PENNEY_DESCRIPTION.split(), 100)))
    line(100)
    tprint("MENU : ")
