import random
from brain_games.games.run_game import run_game

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_is_prime():
    num = random.randint(1, 100)
    correct_answer = 'yes'
    for i in range(2, num // 2):
        if num % i == 0:
            correct_answer = 'no'
            break
    return num, correct_answer


def is_prime():
    run_game(GAME_RULES, generate_is_prime)
