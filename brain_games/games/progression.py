import random
from brain_games.games.run_game import run_game

GAME_RULES = 'What number is missing in the progression?'


def generate_progression():
    num_one, span = random.randint(1, 100), random.randint(3, 10)
    arithmetic_progression = []
    for _ in range(10):
        arithmetic_progression.append(num_one)
        num_one += span
    index = random.randint(1, 9)
    correct_answer = str(arithmetic_progression.pop(index))
    arithmetic_progression.insert(index, '..')
    data = ' '.join(map(str, arithmetic_progression))
    return data, correct_answer


def progression():
    run_game(GAME_RULES, generate_progression)
