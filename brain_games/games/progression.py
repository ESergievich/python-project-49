from brain_games.scripts.ask_question import ask_question
import random


def progression():
    num_one, span = random.randint(1, 100), random.randint(3, 10)
    arithmetic_progression = []
    for _ in range(10):
        arithmetic_progression.append(num_one)
        num_one += span
    index = random.randint(1, 10)
    ans_tusk = arithmetic_progression.pop(index)
    arithmetic_progression.insert(index, '..')
    question = ' '.join(map(str, arithmetic_progression))
    ask_question(question)
    return str(ans_tusk)


def main():
    progression()


if __name__ == '__main__':
    main()
