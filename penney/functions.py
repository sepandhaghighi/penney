# -*- coding: utf-8 -*-
"""Penney functions."""
import random
import time
from .params import *
from art import tprint
import copy


def print_line(number=11, char="#"):
    """
    Print line of char.

    :param number: number of character in this line
    :type number : int
    :param char: character
    :type char : str
    :return: None
    """
    print(char * number)


def justify_left(words, width):
    """
    Left justify words.

    :param words: list of words
    :type words : list
    :param width: width of each line
    :type width: int
    :return: left justified words as list
    """
    return ' '.join(words).ljust(width)


def justify_text(words, width):
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
                yield justify_left(line, width)
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
        yield justify_left(line, width)


def generate_sequence():
    """
    Generate each part of sequence.

    :return: sequence part as str
    """
    return random.choice(["T", "H"])


def find_winner(sequence, player_sequences):
    """
    Identify each round winner.

    :param sequence: round sequence
    :type sequence: str
    :param player_sequences: player sequences
    :type player_sequences: dict
    :return: winner name as str
    """
    winner_name = ""
    min_index = len(sequence)
    for name in player_sequences:
        name_index = sequence.find(player_sequences[name])
        if name_index != -1:
            if name_index < min_index:
                winner_name = name
                min_index = name_index
    if len(winner_name) != 0:
        return winner_name
    return None


def det(A):
    """
    Calculate determinant of a matrix in a fast way.

    :param A: matrix itself
    :type A: list or numpy.array
    :return: determinant of A in float
    """
    n = len(A)
    AM = copy.deepcopy(A)
    for focus_diagonal in range(n):
        for i in range(focus_diagonal + 1, n):
            if AM[focus_diagonal][focus_diagonal] == 0:
                AM[focus_diagonal][focus_diagonal] = 1.0e-18
            row_scaler = AM[i][focus_diagonal] / AM[focus_diagonal][focus_diagonal]
            for j in range(n):
                AM[i][j] = AM[i][j] - row_scaler * AM[focus_diagonal][j]
    determinant = 1.0
    for i in range(n):
        determinant *= AM[i][i]
    return determinant


def calculate_C(player_sequences):
    """
    Calculate C Matrix used in winning probability process.

    :param player_sequences: player sequences
    :type player_sequences: dict
    :return: C Matrix as a 2D list.
    """
    C = []
    names = sorted(player_sequences)

    def p_seq(sequence): return 1 / 2 ** len(sequence)
    for name1 in names:
        A_i = player_sequences[str(name1)]
        C_row = []
        for name2 in names:
            A_j = player_sequences[str(name2)]
            w_i_j = 0
            for k in range(1, min(len(A_i), len(A_j)) + 1):
                if A_i[:k] == A_j[len(A_j) - k:]:
                    w_i_j += p_seq(A_i[k:])
            C_row.append(w_i_j)
        C.append(C_row)
    return C


def calculate_probability(player_sequences):
    """
    Calculate probability of each player.

    :param player_sequences: player sequences
    :type player_sequences: dict
    :return: players win probabilities as a dict.
    """
    prob_dic = {}
    names = sorted(player_sequences)
    C = calculate_C(player_sequences)
    det_dic = {}
    for j, name in enumerate(names):
        C_j = []
        for i in range(len(names)):
            C_j.append([1 if k == j else C[i][k] for k in range(len(names))])
        det_dic[name] = det(C_j)
    sum_det = sum(det_dic.values())
    for name in names:
        prob_dic[name] = det_dic[name] / sum_det
    return prob_dic


def print_probability(prob_dic):
    """
    Print win probabilities of players.

    :param prob_dic: win probability dictionary
    :type prob_dic: dict
    :return: None
    """
    sorted_probs = sorted(
        prob_dic.items(), key=lambda x: (
            x[1], x[0]), reverse=True)
    name_max_length = max(map(len, prob_dic))
    print("Wining Probability : ")
    for item in sorted_probs:
        prob = item[1]
        name = item[0]
        space_name = (name_max_length - len(name) + 5) * " "
        print(name + space_name + "{probability:0.3f}%".format(probability=prob * 100))
    if len(set(prob_dic.values())) > 1:
        print("Winner should be {possible_winner}".format(possible_winner=sorted_probs[0][0]))


def run_game(player_sequences, round_number=100, print_status=False):
    """
    Game simulation.

    :param player_sequences: player sequences
    :type player_sequences: dict
    :param round_number: number of rounds
    :type round_number: int
    :param print_status: print status flag
    :type print_status: bool
    :return: scores as dict
    """
    current_round = 0
    scores = {name: 0 for name in player_sequences}
    while(current_round < round_number):
        next_round = False
        round_sequence = ""
        while(not next_round):
            round_sequence += generate_sequence()
            winner = find_winner(round_sequence, player_sequences)
            if winner is not None:
                if print_status:
                    print("Round {round_number}".format(round_number=str(current_round + 1)))
                    print_sequence(round_sequence)
                    print(POINT_MESSAGE.format(winner=winner))
                    print_line()
                    time.sleep(1)
                scores[winner] += 1
                next_round = True
        current_round += 1
    return scores


def validate_sequence(sequence, sequence_length, player_sequences):
    """
    Check the validity of sequence.

    :param sequence: test sequence
    :type sequence: str
    :param sequence_length: sequence length
    :type sequence_length: int
    :param player_sequences: players sequences
    :type player_sequences: dict
    :return: validity as bool
    """
    sequence_elements = set(list(sequence))
    if len(sequence) == sequence_length and sequence_elements.issubset(
            {"T", "H"}) and sequence not in player_sequences.values():
        return True
    return False


def get_sequence(sequence_length, names_dict, computer_sequence=None):  # pragma: no cover
    """
    Get sequence from user.

    :param sequence_length: sequence length
    :type sequence_length: int
    :param names_dict: players names
    :type names_dict: dict
    :param computer_sequence: computer sequence
    :type computer_sequence: str
    :return: players sequences as dict
    """
    player_sequences = {name: "" for name in names_dict.values()}
    for player_ord in sorted(names_dict):
        while(True):
            player_name = names_dict[player_ord]
            player_sequence = input(SEQUENCE_MESSAGE.format(player_name=str(player_name)))
            if validate_sequence(
                    player_sequence,
                    sequence_length,
                    player_sequences) and player_sequence != computer_sequence:
                player_sequences[player_name] = player_sequence
                break
            else:
                print(SEQUENCE_ERROR.format(sequence_length=str(sequence_length)))
    return player_sequences


def get_length():  # pragma: no cover
    """
    Get sequence length from user.

    :return: sequence length as int
    """
    sequence_length = 0
    while(True):
        try:
            sequence_length = int(input(LENGTH_MESSAGE))
            if sequence_length >= 3:
                break
            else:
                print(LENGTH_ERROR1)
        except Exception:
            print(LENGTH_ERROR2)
    return sequence_length


def validate_name(name, name_list):
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


def get_names(number=2):  # pragma: no cover
    """
    Get names from user.

    :param number: number of players
    :type number: int
    :return: players names as dict
    """
    names_dict = {}
    names_order = list(range(1, number + 1))
    index = 0
    while(index < number):
        while(True):
            name = input(PLAYER_NAME_MESSAGE.format(index=str(index + 1)))
            if validate_name(name, names_dict):
                rand_order = random.choice(names_order)
                names_order.remove(rand_order)
                names_dict[rand_order] = name
                break
            else:
                print(PLAYER_NAME_ERROR)
        index += 1
    return names_dict


def print_result(scores, player_sequences):
    """
    Print game result.

    :param scores: players scores
    :type scores: dict
    :param player_sequences: players sequences
    :type player_sequences: dict
    :return: None
    """
    sorted_scores = sorted(
        scores.items(), key=lambda x: (
            x[1], x[0]), reverse=True)
    name_max_length = max(map(len, scores))
    score_max_length = max(map(lambda x: len(str(x)), scores.values()))
    print("Scores Table : ")
    for item in sorted_scores:
        score = item[1]
        name = item[0]
        space_name = (name_max_length - len(name) + 5) * " "
        space_score = (score_max_length - len(str(score)) + 3) * " "
        print(name + space_name + str(score) + space_score + player_sequences[name])
    if sorted_scores[0][1] != sorted_scores[1][1]:
        print("Winner : {winner}".format(winner=sorted_scores[0][0]))
    else:
        print("Tie!")


def print_sequence(sequence, delay=0.3):
    """
    Print a sequence one by one.

    :param sequence: round sequence
    :type sequence: str
    :param delay: delay between each step
    :type delay: float
    :return: None
    """
    end_str = ""
    sequence_length = len(sequence)
    for index, item in enumerate(sequence):
        if index == (sequence_length - 1):
            end_str = "\n"
        print(item, end=end_str, flush=True)
        time.sleep(delay)


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


def generate_computer_sequence(sequence_length, sequence=None):
    """
    Generate computer sequence.

    :param sequence_length: sequence length
    :type sequence_length: int
    :param sequence: player sequence
    :type sequence: str
    :return: computer sequence as str
    """
    while(True):
        result = ""
        index = 0
        while(index < sequence_length):
            result += generate_sequence()
            index += 1
        if sequence != result or sequence is None:
            break
    return result


def filter_players(number, sequence_length, print_status=False):
    """
    Filter number of players.

    :param number: number of players
    :type number: int
    :param sequence_length: sequence length
    :type sequence_length: int
    :param print_status: print status flag
    :type print_status: bool
    :return: filtered number of players as int
    """
    if number < 2:
        if print_status:
            print(PLAYER_NUMBER_WARNING.format(number_of_players="2"))
        return 2
    if number > 2**sequence_length:
        if print_status:
            print(PLAYER_NUMBER_WARNING.format(number_of_players=str(2**sequence_length)))
        return 2**sequence_length
    return number


def computer_player_handler(sequence_length):  # pragma: no cover
    """
    Computer-Player mode handler.

    :param sequence_length: sequence length
    :type sequence_length: int
    :return: players sequences as dict
    """
    names_dict = get_names(number=1)
    computer_name = "Computer"
    player_name = list(names_dict.values())[0]
    if player_name.upper() == 'COMPUTER':
        computer_name = "Bot"
    computer_sequence = None
    first_coin = generate_sequence()
    if first_coin == "T":
        computer_sequence = generate_computer_sequence(sequence_length)
        print(COMPUTER_SEQUENCE_MESSAGE.format(computer_name=computer_name, computer_sequence=computer_sequence))
    player_sequences = get_sequence(sequence_length, names_dict, computer_sequence)
    player_seq = list(player_sequences.values())[0]
    if computer_sequence is None:
        computer_sequence = generate_computer_sequence(sequence_length, player_seq)
        print(COMPUTER_SEQUENCE_MESSAGE.format(computer_name=computer_name, computer_sequence=computer_sequence))
    player_sequences[computer_name] = computer_sequence
    return player_sequences


def player_player_handler(sequence_length):  # pragma: no cover
    """
    Player-Player mode handler.

    :param sequence_length: sequence length
    :type sequence_length: int
    :return: players sequences as dict
    """
    player_number = get_number(PLAYER_NUMBER_MESSAGE, PLAYER_NUMBER_ERROR)
    player_number = filter_players(
        player_number,
        sequence_length=sequence_length,
        print_status=True)
    names_dict = get_names(number=player_number)
    player_sequences = get_sequence(sequence_length, names_dict)
    return player_sequences


def menu_handler():  # pragma: no cover
    """
    CLI menu main handler.

    :return: None
    """
    fast_sim_flag = False
    tprint("MENU : ")
    player_or_computer = input(PLAYER_COMPUTER_MESSAGE)
    print_line()
    fast_sim_str = input(SIMULATION_MODE_MESSAGE)
    print_line()
    round_number = abs(get_number(ROUND_NUMBER_MESSAGE, ROUND_NUMBER_ERROR))
    sequence_length = get_length()
    if fast_sim_str == "1":
        fast_sim_flag = True
    if player_or_computer != "1":
        player_sequences = player_player_handler(sequence_length)
    else:
        player_sequences = computer_player_handler(sequence_length)
    print_line()
    print_probability(calculate_probability(player_sequences))
    print_line()
    scores = run_game(player_sequences, round_number=round_number, print_status=not fast_sim_flag)
    print_result(scores, player_sequences)


def print_description():  # pragma: no cover
    """
    Print introduction and description.

    :return: None
    """
    tprint("Penney Game", font="larry3d")
    tprint("v {version}".format(version=PENNEY_VERSION))
    print_line(100)
    print("\n".join(justify_text(PENNEY_DESCRIPTION.split(), 100)))
    print_line(100)
