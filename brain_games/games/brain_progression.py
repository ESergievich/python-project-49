import random
import operator
import prompt
from brain_games.scripts import brain_models


def progression():
    name = brain_models.greet()
    print('What number is missing in the progression?')
    for _ in range(3):
        num_one, span = random.randint(1, 100), random.randint(3, 10)
        progress = []
        for _ in range(10):
            progress.append(num_one)
            num_one += span
        index = random.randint(1, 10)
        real_ans = progress.pop(index)
        progress.insert(index, '..')
        print('Question:', *progress, sep=' ')
        ans = prompt.integer('Your answer: ')
        if brain_models.verify(ans, real_ans, name) == 'stop':
            return None
    return brain_models.finish(name)


def main():
    progression()


if __name__ == '__main__':
    main()
