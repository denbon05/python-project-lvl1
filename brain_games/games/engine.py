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
        elif mode == 'game-calc':
            print('What is the result of the expression?')
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            operator = random.choice(('+', '-', '*'))
            number = eval('{}{}{}'.format(num1, operator, num2))
            print('Question: {} {} {}'.format(num1, operator, num2))
        answer = prompt.string('Your answer: ')
        if not utils.is_right_answer(answer, number, mode):
            return print("Let's try again, {}!".format(name))
        print('Correct!')
        count += 1
    print('Congratulations, {}!'.format(name))
