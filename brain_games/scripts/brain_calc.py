import random
import prompt


def even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
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


# brain-calc
#
# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# What is the result of the expression?
# Question: 4 + 10
# Your answer: 14
# Correct!
# Question: 25 - 11
# Your answer: 14
# Correct!
# Question: 25 * 7
# Your answer: 175
# Correct!
# Congratulations, Sam!
# Достаточно реализовать следующие операции: +, - и *
# Операции, как и числа, выбираются случайным образом
# В случае, если пользователь даст неверный ответ, необходимо вывести:
#
# Question: 25 * 7
# Your answer: 145
# '145' is wrong answer ;(. Correct answer was '175'.
# Let's try again, Sam!