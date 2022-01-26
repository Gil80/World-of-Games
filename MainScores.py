from flask import Flask, render_template
from flask import request
from Scores import scores_file
import os

dirname = os.path.dirname(__file__)
score = os.path.abspath('score.html')
error = os.path.abspath('error.html')

        
app = Flask(__name__)
@app.route('/')
def score_server():
    try:
       with open(scores_file,'r', encoding='utf-8') as reader:
           score_file_lines: list = reader.readlines()
           first_line_raw: str = score_file_lines[0]
           first_line: str = first_line_raw.strip()
           score: int = int(first_line)
           return render_template('score.html', SCORE=score)
    except (ValueError, IndexError, FileNotFoundError):
        return render_template('error.html', ERROR="Failed to read score")
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8777) # this line was added for running form docker https://medium.com/@rokinmaharjan/running-a-flask-application-in-docker-80191791e143
