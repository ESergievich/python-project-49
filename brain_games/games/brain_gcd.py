import random
import operator
import prompt
from brain_games.scripts import brain_models


def gcd():
    name = brain_models.greet()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        num_one, num_two = random.randint(1, 100), random.randint(1, 100)
        print(f'Question: {num_one} {num_two}')
        num_one, num_two = max(num_one, num_two), min(num_one, num_two)
        while num_two != 0:
            num_one, num_two = num_two, num_one % num_two
        real_ans = num_one
        ans = prompt.integer('Your answer: ')
        if brain_models.verify(ans, real_ans, name) == 'stop':
            return None
    return brain_models.finish(name)


def main():
    gcd()


if __name__ == '__main__':
    main()
