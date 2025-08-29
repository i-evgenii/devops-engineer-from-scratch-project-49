from random import randint

DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_LENGTH = 10
MAX_INITIAL_VALUE = 20
MIN_STEP, MAX_STEP = -10, 10


def get_question(init_value, step, index_of_hole):
    question = []

    for counter in range(PROGRESSION_LENGTH):
        if counter > 0:
            question.insert(counter, " ")
        if counter == index_of_hole:
            question.insert(counter, "..")
        else:
            current_value = init_value + step * counter
            question.insert(counter, str(current_value))
    return " ".join(question)


def generate_round():
    init_value = randint(0, MAX_INITIAL_VALUE)
    step = randint(MIN_STEP, MAX_STEP)
    index_of_hole = randint(0, PROGRESSION_LENGTH - 1)

    question = get_question(init_value, step, index_of_hole)
    correct_answer = init_value + step * index_of_hole

    return question, str(correct_answer)
