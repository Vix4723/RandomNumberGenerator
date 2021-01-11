# Victoria Clotet
# Local Hack Day: Build 2021 Day 2 Daily Challenge
# Prompt: Many languages contain classes that allow for the functionality of a random number generator, but we want you
# to create your own method that does this. Don't pick a Random Devpost to submit to, submit your hack on our Day 2
# Devpost!

# My method consists on using the actual time in seconds and generating a random number based on the actual seconds

import time


def random_number1():
    """
    This function presents the time in seconds and then divides it by a number within the range of 1 and 50
    :return: a random generated number in seconds
    """
    for i in range(1, 50):
        number = time.time() / i
        return number


def random_number2():
    """
    This function prints the random number
    :return: random number
    """
    seconds = random_number1()
    print("Your random number generator is ", seconds)


def random_number3():
    """
    same functionality as the function random_number1 but I decided to change the range to test the range difference
    between random numbers.
    :return: random number
    """
    for i in range(2, 75):
        num = time.time() / i
        return num


def random_number4():
    """
    This function prints the random number
    :return: random number
    """
    random = random_number3()
    print("Here is another random number: ", random)


random_number2()
random_number4()
