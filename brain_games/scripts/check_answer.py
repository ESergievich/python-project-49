#!/usr/bin/env python3

def check_answer(ans_task, ans_user, user_name):
    flag = True
    if ans_task != ans_user:
        flag = False
        print(f"{ans_user} is wrong answer ;(. Correct answer was {ans_task}.\n"
              f"Let's try again, {user_name}!")
        return flag
    print('Correct!')
    return flag


def main():
    check_answer()


if __name__ == 'main':
    main()
