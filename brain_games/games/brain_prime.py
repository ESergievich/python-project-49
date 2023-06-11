import random
import operator
import prompt
from brain_games.scripts import brain_models


def prime():
    name = brain_models.greet()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        num_one = random.randint(1, 100)
        real_ans = 'yes'
        for i in range(2, num_one // 2):
            if num_one % i == 0:
                real_ans = 'no'
                break
        print(f'Question: {num_one}')
        ans = prompt.string('Your answer: ')
        if brain_models.verify(ans, real_ans, name) == 'stop':
            return None
    return brain_models.finish(name)


def main():
    prime()


if __name__ == '__main__':
    main()




# brain-prime
#
# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# Answer "yes" if given number is prime. Otherwise answer "no".
# Question: 7
# Your answer: yes
# Correct!