from random import randint
from Utils import screen_cleaner
import time
from Scores import add_score


# generating random numbers in range and stores them in a list.
def generate_sequence(difficulty):
    rand_list = []
    for number in range(1, difficulty + 1):
        rand_list.append(randint(1, 101))
    return rand_list


# asks user to input numbers and validates the input.
def get_list_from_user(difficulty):
    list_from_user = []
    int_list_from_user = []
    for i in range(1, difficulty + 1):
        num = "th"

        if i == 1:
            num = "st"
        elif i == 2:
            num = "nd"
        elif i == 3:
            num = "rd"
        list_from_user.append(input(f"type the {i}{num} number and press ENTER:\n"))

        #  trying to catch if user doesn't enter numbers
        try:
            int_list_from_user = list(map(int, list_from_user))  # using map() to perform conversion
        except ValueError:
            print("You didn't type a valid number. Try again.")
            return get_list_from_user(difficulty)

        #  validated numbers are between 1 and 101.
        for c in range(len(int_list_from_user)):
            if int_list_from_user[c] <= 0 or int_list_from_user[c] > 101:
                print("Number is out of range. Start over.")
                return get_list_from_user(difficulty)

    return int_list_from_user


# compares program random selections to user input selection.
def is_list_equal(rand_list, int_list_from_user):
    return rand_list == int_list_from_user  # will return True or False


# passes the difficulty level. calls other game functions. print results.
def play(difficulty):
    rand_list = generate_sequence(difficulty)
    input("Press Enter to start")
    print(rand_list)
    time.sleep(0.7)
    screen_cleaner()
    #print('\n' * 100)  # faking clear screen for pycharm
    int_list_from_user = get_list_from_user(difficulty)
    result = is_list_equal(rand_list, int_list_from_user)
    print(f"The comparison is: {result}")
    print(f"The computer generated these numbers: {rand_list}")
    if result:
        add_score(difficulty)
        print("You remembered all the numbers. You Win!")
    else:
        print("You didn't remember all the numbers. You lose.")
    return result



