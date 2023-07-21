import prompt


def welcome_user(game_rules):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_rules)
    return user_name


def get_answer(question):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    return user_answer


def check_answer(user_answer, correct_answer, user_name):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    print(f"""
{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.
Let's try again, {user_name}!
""")
    return False


def congratulations(user_name):
    print(f'Congratulations, {user_name}!')
