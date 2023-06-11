#!/usr/bin/env python3

import random
import prompt
from scripts.greet import greet


def even():
    greet()
    for _ in range(3):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        ans = prompt.string('Your answer: ')
        if num % 2 == 0:
            real_answ = 'yes'
        else:
            real_answ = 'no'
        if real_answ == ans:
            print('Correct!')
        else:
            return f"""{ans} is wrong answer ;(. Correct answer was {real_answ}.
Let's try again, {name}!"""
    return f'Congratulations, {name}!'


def main():
    print(even())


if __name__ == '__main__':
    main()
