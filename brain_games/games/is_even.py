#!/usr/bin/env python3

from brain_games.scripts.ask_question import ask_question
import random


def is_even():
    num = random.randint(1, 100)
    question = f'{num}'
    ask_question(question)
    if num % 2 == 0:
        return 'yes'
    return 'no'


def main():
    is_even()


if __name__ == '__main__':
    main()
