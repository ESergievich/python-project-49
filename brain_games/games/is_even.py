import random
from brain_games.games.run_game import run_game

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_is_even():
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return number, correct_answer


def is_even():
    run_game(GAME_RULES, generate_is_even)
