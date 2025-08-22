# -*- coding: utf-8 -*-
"""Penney functions."""
from typing import Dict, List, Optional, Iterator
import random
import time
from .params import *
from art import tprint
import copy


def print_line(number: int = 11, char: str = "#") -> None:
    """
    Print line of char.

    :param number: number of character in this line
    :param char: character
    """
    print(char * number)


def justify_left(words: List[str], width: int) -> str:
    """
    Left justify words.

    :param words: list of words
    :param width: width of each line
    """
    return ' '.join(words).ljust(width)


def justify_text(words: List[str], width: int) -> Iterator[str]:
    """
    Justify input words.

    :param words: list of words
    :param width: width of each line
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


def generate_sequence() -> str:
    """Generate each part of sequence."""
    return random.choice(["T", "H"])


def find_winner(sequence: str, player_sequences: Dict[str, str]) -> str:
    """
    Identify each round winner.

    :param sequence: round sequence
    :param player_sequences: player sequences
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


def calculate_determinant(matrix: List[float]) -> float:
    """
    Calculate determinant of a matrix in a fast way.

    :param matrix: matrix itself
    """
    n = len(matrix)
    matrix_copy = copy.deepcopy(matrix)
    for focus_diagonal in range(n):
        for i in range(focus_diagonal + 1, n):
            if matrix_copy[focus_diagonal][focus_diagonal] == 0:
                matrix_copy[focus_diagonal][focus_diagonal] = 1.0e-18
            row_scaler = matrix_copy[i][focus_diagonal] / matrix_copy[focus_diagonal][focus_diagonal]
            for j in range(n):
                matrix_copy[i][j] = matrix_copy[i][j] - row_scaler * matrix_copy[focus_diagonal][j]
    determinant = 1.0
    for i in range(n):
        determinant *= matrix_copy[i][i]
    return determinant


def calculate_C(player_sequences: Dict[str, str]) -> List[List[int]]:
    """
    Calculate C Matrix used in winning probability process.

    :param player_sequences: player sequences
    """
    C = []
    names = sorted(player_sequences)
    def calculate_sequence_probability(sequence): return 1 / 2 ** len(sequence)
    for name1 in names:
        A_i = player_sequences[str(name1)]
        C_row = []
        for name2 in names:
            A_j = player_sequences[str(name2)]
            w_i_j = 0
            for k in range(1, min(len(A_i), len(A_j)) + 1):
                if A_i[:k] == A_j[len(A_j) - k:]:
                    w_i_j += calculate_sequence_probability(A_i[k:])
            C_row.append(w_i_j)
        C.append(C_row)
    return C


def calculate_probability(player_sequences: Dict[str, str]) -> Dict[str, float]:
    """
    Calculate probability of each player.

    :param player_sequences: player sequences
    """
    probability_dict = {}
    names = sorted(player_sequences)
    C = calculate_C(player_sequences)
    determinant_dict = {}
    for j, name in enumerate(names):
        C_j = []
        for i in range(len(names)):
            C_j.append([1 if k == j else C[i][k] for k in range(len(names))])
        determinant_dict[name] = calculate_determinant(C_j)
    determinant_sum = sum(determinant_dict.values())
    for name in names:
        probability_dict[name] = determinant_dict[name] / determinant_sum
    return probability_dict


def print_probability(probability_dict: Dict[str, float]) -> None:
    """
    Print win probabilities of players.

    :param probability_dict: win probability dictionary
    """
    probabilities = sorted(
        probability_dict.items(), key=lambda x: (
            x[1], x[0]), reverse=True)
    name_max_length = max(map(len, probability_dict))
    print("Wining Probability : ")
    for item in probabilities:
        probability = item[1]
        name = item[0]
        space_name = (name_max_length - len(name) + 5) * " "
        print(name + space_name + "{probability:0.3f}%".format(probability=probability * 100))
    if len(set(probability_dict.values())) > 1:
        print("Winner should be {possible_winner}".format(possible_winner=probabilities[0][0]))


def run_game(player_sequences: Dict[str, str], round_number: int = 100, print_status: bool = False) -> Dict[str, int]:
    """
    Game simulation.

    :param player_sequences: player sequences
    :param round_number: number of rounds
    :param print_status: print status flag
    """
    current_round = 0
    scores = {name: 0 for name in player_sequences}
    while current_round < round_number:
        next_round = False
        round_sequence = ""
        while not next_round:
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


def validate_sequence(sequence: str, sequence_length: int, player_sequences: Dict[str, str]) -> bool:
    """
    Check the validity of sequence.

    :param sequence: test sequence
    :param sequence_length: sequence length
    :param player_sequences: players sequences
    """
    sequence_elements = set(list(sequence))
    if len(sequence) == sequence_length and sequence_elements.issubset(
            {"T", "H"}) and sequence not in player_sequences.values():
        return True
    return False


def get_sequence(sequence_length: int, names_dict: Dict[int, str], computer_sequence: Optional[str] = None) -> Dict[str, str]:  # pragma: no cover
    """
    Get sequence from user.

    :param sequence_length: sequence length
    :param names_dict: players names
    :param computer_sequence: computer sequence
    """
    player_sequences = {name: "" for name in names_dict.values()}
    for player_index in sorted(names_dict):
        while True:
            player_name = names_dict[player_index]
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


def get_length() -> int:  # pragma: no cover
    """Get sequence length from user."""
    sequence_length = 0
    while True:
        try:
            sequence_length = int(input(LENGTH_MESSAGE))
            if sequence_length >= 3:
                break
            else:
                print(LENGTH_ERROR1)
        except Exception:
            print(LENGTH_ERROR2)
    return sequence_length


def validate_name(name: str, names_list: List[str]) -> bool:
    """
    Check the validity of name.

    :param name: test name
    :param names_list: players names
    """
    if len(name) != 0 and name not in names_list:
        return True
    return False


def get_names(number: int = 2) -> Dict[int, str]:  # pragma: no cover
    """
    Get names from user.

    :param number: number of players
    """
    names_dict = {}
    names_order = list(range(1, number + 1))
    index = 0
    while index < number:
        while True:
            name = input(PLAYER_NAME_MESSAGE.format(index=str(index + 1)))
            if validate_name(name, names_dict):
                random_order = random.choice(names_order)
                names_order.remove(random_order)
                names_dict[random_order] = name
                break
            else:
                print(PLAYER_NAME_ERROR)
        index += 1
    return names_dict


def print_result(scores: Dict[str, int], player_sequences: Dict[str, str]) -> None:
    """
    Print game result.

    :param scores: players scores
    :param player_sequences: players sequences
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


def print_sequence(sequence: str, delay: float = 0.3) -> None:
    """
    Print a sequence one by one.

    :param sequence: round sequence
    :param delay: delay between each step
    """
    end_str = ""
    sequence_length = len(sequence)
    for index, item in enumerate(sequence):
        if index == (sequence_length - 1):
            end_str = "\n"
        print(item, end=end_str, flush=True)
        time.sleep(delay)


def get_number(message: str, error_message: str) -> int:  # pragma: no cover
    """
    Get a number from user.

    :param message: user message
    :param error_message: error message
    """
    number = 0
    while True:
        try:
            number = int(input(message))
            break
        except Exception:
            print(error_message)
    return number


def generate_computer_sequence(sequence_length: int, sequence: Optional[str] = None) -> str:
    """
    Generate computer sequence.

    :param sequence_length: sequence length
    :param sequence: player sequence
    """
    while True:
        result = ""
        index = 0
        while index < sequence_length:
            result += generate_sequence()
            index += 1
        if sequence != result or sequence is None:
            break
    return result


def filter_players(number: int, sequence_length: int, print_status: bool = False) -> int:
    """
    Filter number of players.

    :param number: number of players
    :param sequence_length: sequence length
    :param print_status: print status flag
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


def computer_player_handler(sequence_length: int) -> Dict[str, str]:  # pragma: no cover
    """
    Computer-Player mode handler.

    :param sequence_length: sequence length
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


def player_player_handler(sequence_length: int) -> Dict[str, str]:  # pragma: no cover
    """
    Player-Player mode handler.

    :param sequence_length: sequence length
    """
    player_number = get_number(PLAYER_NUMBER_MESSAGE, PLAYER_NUMBER_ERROR)
    player_number = filter_players(
        player_number,
        sequence_length=sequence_length,
        print_status=True)
    names_dict = get_names(number=player_number)
    player_sequences = get_sequence(sequence_length, names_dict)
    return player_sequences


def menu_handler() -> None:  # pragma: no cover
    """CLI menu main handler."""
    fast_simulation_flag = False
    tprint("MENU : ")
    player_or_computer = input(PLAYER_COMPUTER_MESSAGE)
    print_line()
    fast_simulation_str = input(SIMULATION_MODE_MESSAGE)
    print_line()
    round_number = abs(get_number(ROUND_NUMBER_MESSAGE, ROUND_NUMBER_ERROR))
    sequence_length = get_length()
    if fast_simulation_str == "1":
        fast_simulation_flag = True
    if player_or_computer != "1":
        player_sequences = player_player_handler(sequence_length)
    else:
        player_sequences = computer_player_handler(sequence_length)
    print_line()
    print_probability(calculate_probability(player_sequences))
    print_line()
    scores = run_game(player_sequences, round_number=round_number, print_status=not fast_simulation_flag)
    print_result(scores, player_sequences)


def print_description() -> None:  # pragma: no cover
    """Print introduction and description."""
    tprint("Penney Game", font="larry3d")
    tprint("v {version}".format(version=PENNEY_VERSION))
    print_line(100)
    print("\n".join(justify_text(PENNEY_DESCRIPTION.split(), 100)))
    print_line(100)
