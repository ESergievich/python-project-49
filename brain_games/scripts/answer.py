def answer(ans, real_ans, name):
    if real_ans == ans:
        print('Correct!')
    else:
        return f"""{ans} is wrong answer ;(. Correct answer was {real_ans}.
    Let's try again, {name}!"""
    return f'Congratulations, {name}!'


def main():
    answer(ans, real_ans, name)


if __name__ == 'main':
    main()
