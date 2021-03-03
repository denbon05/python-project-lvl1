import random
from math import gcd


def is_even(number):
    return number % 2 == 0


def is_right_answer(answer, number, mode):
    if mode == 'even-game':
        is_allowable_answer = answer in ('yes', 'no')
        is_correct_answer = is_even(number) and answer == 'yes' \
            or not is_even(number) and answer == 'no'
        return is_allowable_answer and is_correct_answer
    elif mode == 'game-calc' or 'game-gcd':
        return int(answer) == number


def print_feed(name, answer, number, mode):
    if mode == 'even-game':
        return print("Let's try again, {}!".format(name))
    else:
        return print(
            ("'{}' is wrong answer ;(. Correct answer was '{}'.")
            .format(answer, number)
        )


def brain_even_handler():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number = random.randint(1, 100)
    print('Question: {}'.format(number))
    return number


def brain_calc_handler():
    print('What is the result of the expression?')
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 20)
    operator = random.choice(('+', '-', '*'))
    number = eval('{}{}{}'.format(num1, operator, num2))
    print('Question: {} {} {}'.format(num1, operator, num2))
    return number


def brain_gcd_handler():
    print('Find the greatest common divisor of given numbers.')
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    number = gcd(num1, num2)
    print('Question: {} {}'.format(num1, num2))
    return number
