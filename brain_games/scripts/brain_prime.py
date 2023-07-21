#!/usr/bin/env python3

from brain_games.games.is_prime import is_prime
from brain_games.scripts.greet import greet
from brain_games.scripts.check_answer import check_answer
from brain_games.scripts.congratulation import congratulations
from brain_games.scripts.get_answer import get_answer


def brain_prime():
    user_name = greet()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        ans_task = is_prime()
        ans_user = get_answer()
        if not check_answer(ans_task, ans_user, user_name):
            return
    congratulations(user_name)


def main():
    brain_prime()


if __name__ == '__main__':
    main()
