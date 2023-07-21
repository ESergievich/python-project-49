#!/usr/bin/env python3

import prompt


def get_answer():
    return prompt.string('Your answer: ')


def main():
    get_answer()


if __name__ == '__main__':
    main()
