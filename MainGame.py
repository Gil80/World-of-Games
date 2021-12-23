import Utils
from Live import load_game
from GuessGame import play as gg
from MemoryGame import play as mg
from CurrencyRouletteGame import play as cr

scores_file = Utils.scores_file_name #  path to scores.txt

# reset the scores.txt file
def rest_scores():
    with open(scores_file,'w', encoding='utf-8') as writer:
        writer.write("0")


rest_scores()


game_num, difficulty = load_game()


def start_game(game_num_in, difficulty_in):
    if game_num_in == 1:
        mg(difficulty_in)
    elif game_num_in == 2:
        gg(difficulty_in)
    elif game_num_in == 3:
        cr(difficulty_in)

    ask_if_replay(game_num_in, difficulty_in)


# ask if want to replay the game or go back.
def ask_if_replay(game_num_in, difficulty_in):
    retry_selection = input("Would you like to retry?\nPress 'Y' to retry or 'N' to go back or 'E' to exit: ").lower()

    if retry_selection == 'y':
        start_game(game_num_in, difficulty_in)
    elif retry_selection == 'n':
        local_game_num, local_difficulty = load_game()
        start_game(local_game_num, local_difficulty)
    elif retry_selection == 'e':
        print("Goodbye.")
        exit()
    else:
        print("Invalid selection.", ask_if_replay(difficulty))



start_game(game_num, difficulty)
