#!/usr/bin/env python3

from brain_games.cli import welcome_user


def greet():
    print('poetry run python -m brain_games.scripts.brain_games')
    print('Welcome to the Brain Games!')


def main():
    greet()
    welcome_user()


if __name__ == '__main__':
    main()
