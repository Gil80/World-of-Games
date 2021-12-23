import click
import os

dirname = os.path.dirname(__file__)
scores_file_name = os.path.abspath('Scores.txt')

# function to clear screen
def screen_cleaner():
    click.clear()
    

#scores_file_name = "WorldOfGames/Scores.txt"
bad_return_code = -1
