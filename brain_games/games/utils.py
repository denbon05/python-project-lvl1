def is_even(number):
    return number % 2 == 0


def is_right_answer(answer, number, mode):
    if mode == 'even-game':
        is_allowable_answer = answer in ('yes', 'no')
        is_correct_answer = is_even(number) and answer == 'yes' \
            or not is_even(number) and answer == 'no'
        return is_allowable_answer and is_correct_answer
    elif mode == 'game-calc':
        return int(answer) == number
