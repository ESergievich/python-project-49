#!/usr/bin/env python3

from brain_games.games.calculate import calculate
from brain_games.scripts.greet import greet
from brain_games.scripts.check_answer import check_answer
from brain_games.scripts.congratulation import congratulations
from brain_games.scripts.get_answer import get_answer


def brain_calc():
    user_name = greet()
    print('What is the result of the expression?')
    for _ in range(3):
        ans_task = calculate()
        ans_user = get_answer()
        if not check_answer(ans_task, ans_user, user_name):
            return
    congratulations(user_name)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
