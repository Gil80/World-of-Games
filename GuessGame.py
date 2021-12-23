from random import randint
from Scores import add_score


# generates random secret number
def generate_number(difficulty_input):
    secret_number = randint(1, difficulty_input)
    return secret_number


# prompts the user to guess a number
def get_guess_from_user(difficulty_input):
    try:
        user_guess = int(input(f"Guess a number between 1 to {difficulty_input}: "))
        if user_guess <= 0 or user_guess > difficulty_input:
            print("Number is out of range. Try again.")
            return get_guess_from_user(difficulty_input)
        else:
            return user_guess
    except ValueError:
        print("You didn't type a valid number. Try again.")
        return get_guess_from_user(difficulty_input)


# comparing random number with user input
def compare_results(secret_number, user_guess):
    return secret_number == user_guess  # will return True or False


# runs the game and returns result
def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    print(f"secret number = {secret_number}")  # comment in to test the code
    print(f"Your guess = {user_guess}")
    result = compare_results(secret_number, user_guess)
    print(f"The comparison is: {result}")
    if result:
        print("You guessed correctly!")
        add_score(difficulty)
    else:
        print("You didn't guess the correct number")
    return result
