from brain_games.scripts.ask_question import ask_question
import random


def gcd():
    num_one, num_two = random.randint(1, 100), random.randint(1, 100)
    question = f'{num_one} {num_two}'
    ask_question(question)
    num_one, num_two = max(num_one, num_two), min(num_one, num_two)
    while num_two != 0:
        num_one, num_two = num_two, num_one % num_two
    return str(num_one)


def main():
    gcd()


if __name__ == '__main__':
    main()
