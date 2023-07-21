from brain_games.cli import welcome_user, get_answer, check_answer, \
    congratulations


def run_game(game_rules, generate_game):
    user_name = welcome_user(game_rules)
    for _ in range(3):
        data, correct_answer = generate_game()
        user_answer = get_answer(data)
        if not check_answer(user_answer, correct_answer, user_name):
            return
    congratulations(user_name)
