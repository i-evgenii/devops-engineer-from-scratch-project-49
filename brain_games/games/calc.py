import operator
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'
SIGNS = '-+*'

def calculate(sign, number_a, number_b):

    if sign == '-':
        operation = operator.sub
    elif sign == '+':
        operation = operator.add
    elif sign == '*':
        operation = operator.mul
    return operation(number_a, number_b)


def generate_round():
    
    number_a = randint(1, 10)
    number_b = randint(1, 10)

    sign = choice(SIGNS)
    question = f'{number_a} {sign} {number_b}'
    correct_answer = calculate(sign, number_a, number_b)

    return question, str(correct_answer)
