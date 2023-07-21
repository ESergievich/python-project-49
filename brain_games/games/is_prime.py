from brain_games.scripts.ask_question import ask_question
import random


def is_prime():
    num = random.randint(1, 100)
    question = f'{num}'
    ask_question(question)
    for i in range(2, num // 2):
        if num % i == 0:
            return 'no'
    return 'yes'


def main():
    is_prime()


if __name__ == '__main__':
    main()
