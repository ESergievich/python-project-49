import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def verify(ans, real_ans, name):
    if real_ans == ans:
        print('Correct!')
        return 'next'
    else:
        print(f"""{ans} is wrong answer ;(. Correct answer was {real_ans}.
Let's try again, {name}!""")
        return 'stop'


def finish(name):
    print(f'Congratulations, {name}!')

