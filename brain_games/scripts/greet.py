#!/usr/bin/env python3

import prompt


def greet():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def main():
    greet()


if __name__ == '__main__':
    main()
