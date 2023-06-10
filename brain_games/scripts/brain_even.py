#!/usr/bin/env python3

import random
import prompt


def even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answ = prompt.string('Your answer: ')
        if num % 2 == 0:
            real_answ = 'yes'
        else:
            real_answ = 'no'
        if real_answ == answ:
            print('Correct!')
        else:
            return f"""{answ} is wrong answer ;(. Correct answer was {real_answ}.
Let's try again, {name}!"""
    return f'Congratulations, {name}!'


def main():
    print(even())


if __name__ == '__main__':
    main()
