from random import randint


def six_digit_number():

    six_digit_number = ""
    for num in range(6):
        six_digit_number += str(randint(0, 9))

    return six_digit_number
