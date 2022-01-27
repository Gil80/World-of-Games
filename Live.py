# World Of Games #
from wog_art import logo


def welcome(name):
    if len(name) < 30:
        return print("\nHello " + name + " and welcome to the World Of Games (WoG).\nHere you can find many cool games "
                                         "to play.\n")
    else:
        print("ERROR!!!\nYou have typed more than 30 characters.\nIt's not likely you have such a long name. Please "
              "try again.")
        input_name_try = input("Please type in your name: \n")
        return welcome(input_name_try)


def load_game():
    print("Please choose a game to play:\n")
    game = input("1. Memory game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                 "2. Guess Game - guess a number and see if you choose like the computer\n"
                 "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    if game.isdigit() and 0 < int(game) <= 3:
        game = int(game)
        #  print game selection
        if game == 1:
            print("Your game selection is: Memory Game\n")
        elif game == 2:
            print("Your game selection is: Guess Game\n")
        else:
            print("Your game selection is: Currency Roulette\n")
        while True:
            difficulty_level = input("Please choose game difficulty from 1 to 5:\n")
            if difficulty_level.isdigit() and 0 < int(difficulty_level) <= 5:
                print(f"Your difficulty level is: {difficulty_level}")  # print difficulty selection
                return game, int(difficulty_level)
            else:
                print("\nERROR! You have entered an invalid `difficulty` value. Please try again")
    else:
        print("\nERROR! You have entered an invalid `game` selection. Please try again")
        return load_game()


print(logo)
print('\n' * 2)
input_name = input("Please type in your name: \n")
welcome(input_name)
