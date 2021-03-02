import random
import prompt
from brain_games import welcome_user
from brain_games.games import utils


def start_game(mode):
    name = welcome_user()
    count = 1
    while count <= 3:
        if mode == 'even-game':
            print('Answer "yes" if the number is even, otherwise answer "no".')
            number = random.randint(1, 100)
            print('Question: {}'.format(number))
            answer = prompt.string('Your answer: ')
            if not utils.is_right_answer(answer, number):
                return print("Let's try again, {}!".format(name))
            print('Correct!')
        elif mode == 'game-calc':
            print('Calc game!!!')
        count += 1
    print('Congratulations, {}!'.format(name))
