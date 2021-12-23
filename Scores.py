import io
import Utils



scores_file = Utils.scores_file_name


# The function will try to read the current score in scores.txt file.
# if it fails, it will create a new file and use it to save the current score.
def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    with open(scores_file,'r', encoding='utf-8') as reader:
        current_score_string = reader.read()
        if(current_score_string == ''):
            current_score=0
        else:
            current_score = int(current_score_string)
    
    with open(scores_file,'w', encoding='utf-8') as writer:
        new_score = current_score + points_of_winning
        new_score = str(new_score)
        writer.write(new_score)
