import random
from brain_games.games.run_game import run_game

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def generate_gcd():
    num_one, num_two = random.randint(1, 100), random.randint(1, 100)
    data = f"{num_one} {num_two}"
    while num_two != 0:
        num_one, num_two = num_two, num_one % num_two
    correct_answer = str(num_one)
    return data, correct_answer


def gcd():
    run_game(GAME_RULES, generate_gcd)
