from random import randint

DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_LENGTH = 10
MAX_INITIAL_VALUE = 20
MIN_STEP, MAX_STEP = -10, 10


def get_question(init_value, step, index_of_hole):
    progression = [init_value + step * i for i in range(PROGRESSION_LENGTH)]

    progression[index_of_hole] = ".."

    return " ".join(str(item) for item in progression)


def generate_round():
    init_value = randint(0, MAX_INITIAL_VALUE)
    step = randint(MIN_STEP, MAX_STEP)
    index_of_hole = randint(0, PROGRESSION_LENGTH - 1)

    question = get_question(init_value, step, index_of_hole)
    correct_answer = init_value + step * index_of_hole

    return question, str(correct_answer)
