import random
import prompt
from brain_games import welcome_user


def is_even(number):
    return number % 2 == 0


def is_right_answer(answer, number):
    is_allowable_answer = answer in ('yes', 'no')
    is_correct_answer = is_even(number) and answer == 'yes' \
        or not is_even(number) and answer == 'no'
    return is_allowable_answer and is_correct_answer


def brain_game_even(start_range=1, end_range=100):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 1
    while count <= 3:
        number = random.randint(start_range, end_range)
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        if not is_right_answer(answer, number):
            print("Let's try again, {}!".format(name))
            return False
        count += 1
        print('Correct!')
    print('Congratulations, {}!'.format(name))
    return True
