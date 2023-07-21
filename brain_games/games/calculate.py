import random
import operator
from brain_games.games.run_game import run_game

GAME_RULES = 'What is the result of the expression?'


def generate_calculate():
    num_one, num_two = random.randint(1, 100), random.randint(1, 100)
    op = random.choice(['+', '-', '*'])
    op_func = {
        '+': str(operator.add(num_one, num_two)),
        '-': str(operator.sub(num_one, num_two)),
        '*': str(operator.mul(num_one, num_two))
    }
    data = f"{num_one} {op} {num_two}"
    correct_answer = op_func[op]
    return data, correct_answer


def calculate():
    run_game(GAME_RULES, generate_calculate)
