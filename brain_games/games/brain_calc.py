import random
import operator
import prompt
from brain_games.scripts import brain_models


def calc():
    name = brain_models.greet()
    for _ in range(3):
        num_one, num_two = random.randint(1, 100), random.randint(1, 100)
        op = random.choice(['+', '-', '*'])
        op_func = {
                    '+': operator.add(num_one, num_two),
                    '-': operator.sub(num_one, num_two),
                    '*': operator.mul(num_one, num_two)
                    }
        print(f'Question: {num_one} {op} {num_two}')
        real_ans = op_func[op]
        ans = prompt.integer('Your answer: ')
        if brain_models.verify(ans, real_ans, name) == 'stop':
            return None
    return brain_models.finish(name)


def main():
    calc()


if __name__ == '__main__':
    main()
