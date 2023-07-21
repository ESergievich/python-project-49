from brain_games.scripts.ask_question import ask_question
import random
import operator


def calculate():
    num_one, num_two = random.randint(1, 100), random.randint(1, 100)
    op = random.choice(['+', '-', '*'])
    op_func = {
        '+': operator.add(num_one, num_two),
        '-': operator.sub(num_one, num_two),
        '*': operator.mul(num_one, num_two)
    }
    question = f'{num_one} {op} {num_two}'
    ask_question(question)
    return str(op_func[op])


def main():
    calculate()


if __name__ == '__main__':
    main()
