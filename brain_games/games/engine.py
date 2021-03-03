import prompt
from brain_games import welcome_user
from brain_games.games import utils


def start_game(mode):
    name = welcome_user()
    count = 1
    while count <= 3:
        if mode == 'even-game':
            number = utils.brain_even_handler()
        elif mode == 'game-calc':
            number = utils.brain_calc_handler()
        elif mode == 'game-gcd':
            number = utils.brain_gcd_handler()
        answer = prompt.string('Your answer: ')
        if not utils.is_right_answer(answer, number, mode):
            return utils.print_feed(name, answer, number, mode)
        print('Correct!')
        count += 1
    print('Congratulations, {}!'.format(name))
