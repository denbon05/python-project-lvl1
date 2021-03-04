import prompt
import sys
from brain_games import welcome_user
from brain_games.games import utils


# ! should be flexible path
def start_game(mode):
    run_game = getattr(
        sys.modules['brain_games.games.utils'], '%s_handler' % mode
    )
    name = welcome_user()
    count = 1
    utils.print_game_task(mode)
    while count <= 3:
        number = run_game()
        answer = prompt.string('Your answer: ')
        if not utils.is_right_answer(number, mode, answer):
            return utils.print_feed(name, answer, number, mode)
        print('Correct!')
        count += 1
    print('Congratulations, {}!'.format(name))
