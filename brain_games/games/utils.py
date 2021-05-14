import random
from math import gcd


def print_game_task(mode):
    if mode == 'game_even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif mode == 'game_calc':
        print('What is the result of the expression?')
    elif mode == 'game_gcd':
        print('Find the greatest common divisor of given numbers.')
    elif mode == 'game_progresiion':
        print('What number is missing in the progression?')
    elif mode == 'game_prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number <= 1:
        return False
    counter = 2
    while counter <= number // 2:
        if number == counter:
            return True
        if number % counter == 0:
            return False
        counter += 1
    return True


def is_right_answer(number, mode, answer=None):
    is_allowable_answer = answer in ('yes', 'no')
    if mode == 'game_prime':
        return is_allowable_answer and is_prime(number) and answer == 'yes' \
            or not is_prime(number) and answer == 'no'
    if mode != 'game_even':
        return int(answer) == number
    is_correct_answer = is_even(number) and answer == 'yes' \
        or not is_even(number) and answer == 'no'
    return is_allowable_answer and is_correct_answer


def print_feed(name, answer, number):
    print(
        ("'{}' is wrong answer ;(. Correct answer was '{}'.")
        .format(answer, number)
    )
    print("Let's try again, {}!".format(name))


def game_even_handler():
    number = random.randint(1, 100)
    print('Question: {}'.format(number))
    return number


def game_calc_handler():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 20)
    operator = random.choice(('+', '-', '*'))
    number = eval('{}{}{}'.format(num1, operator, num2))
    print('Question: {} {} {}'.format(num1, operator, num2))
    return number


def game_gcd_handler():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    number = gcd(num1, num2)
    print('Question: {} {}'.format(num1, num2))
    return number


def game_progression_handler():
    count = 0
    current_number = random.randint(1, 50)
    step_value = random.randint(1, 3)
    random_idx = random.randint(0, 9)
    numbers = ()
    while count < 10:
        if count == random_idx:
            num_for_answer = current_number
            numbers += ('..',)
        else:
            numbers += (str(current_number),)
        current_number += step_value
        count += 1
    print('Question: {}'.format(' '.join(numbers)))
    return num_for_answer


def game_prime_handler():
    number = random.randint(1, 100)
    print('Question: {}'.format(number))
    return number
