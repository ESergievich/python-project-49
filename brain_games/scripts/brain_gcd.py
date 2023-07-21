#!/usr/bin/env python3

from brain_games.games.gcd import gcd
from brain_games.scripts.greet import greet
from brain_games.scripts.check_answer import check_answer
from brain_games.scripts.congratulation import congratulations
from brain_games.scripts.get_answer import get_answer


def brain_gcd():
    user_name = greet()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        ans_task = gcd()
        ans_user = get_answer()
        if not check_answer(ans_task, ans_user, user_name):
            return
    congratulations(user_name)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
