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
    with open(scores_file,'r', encoding='utf-8') as reader:
        current_score_string = reader.read()
    return render_template('score.html', SCORE=current_score_string)

@app.route('/')
def error_server():
    with open(scores_file,'r', encoding='utf-8') as reader:
        current_score_string = reader.read()
    return render_template('error.html', ERROR=error)

if __name__ == "__main__":
    app.run()