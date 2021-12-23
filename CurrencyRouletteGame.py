from random import randint
import requests
from Scores import add_score


# get request  currency conversion and interval calculation
def get_money_interval(random_number, difficulty):
    from_currency = 'USD'
    to_currency = 'ILS'

    # Where USD is the base currency you want to use
    url = f'https://v6.exchangerate-api.com/v6/e01de27e3fb2e4ac40d77e31/pair/{from_currency}/{to_currency}'

    # Making our request
    response = requests.get(url)  # entire payload
    data = response.json()  # parsing the json data

    # Your JSON object
    conversion_rate_var = data['conversion_rate']
    print(f"Conversion Rate: {conversion_rate_var}")
    total = int(random_number * conversion_rate_var)  # casting to integer for simplicity
    interval = total - (5 - difficulty), total + (5 - difficulty)
    return interval


# generate a random number from 1 to 100 inclusive
def generate_number():
    random_number = randint(1, 100)
    return random_number


# prompts the user to guess a number
def get_guess_from_user():
    try:
        user_guess = int(input("Guess a number between 1 to 350:\n"))
        if user_guess <= 0 or user_guess > 350:
            print("Number is out of range. Try again.")
            return get_guess_from_user()
        else:
            return user_guess
    except ValueError:
        print("You didn't type a valid number. Try again.")
        return get_guess_from_user()


def play(difficulty):
    random_number = generate_number()
    interval = get_money_interval(random_number, difficulty)
    user_guess = get_guess_from_user()
    min_range = interval[0]
    max_range = interval[1]
    if min_range <= user_guess <= max_range:
        print("You WIN!")
        add_score(difficulty)
    else:
        print("You LOOSE!")
    print(f"The computer generated interval = {interval}")


