import prompt
import sys


def welcome_user():
    print(sys.argv)
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name
