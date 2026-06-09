import csv
import json
import random

GAME_DATA_FILE = "data/game_data.json"


# ==========================================
# LOAD GAME DATA
# ==========================================

def load_game_data():

    with open(
        GAME_DATA_FILE,
        "r"
    ) as f:

        return json.load(f)


# ==========================================
# SAVE GAME DATA
# ==========================================

def save_game_data(data):

    with open(
        GAME_DATA_FILE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


# ==========================================
# LOAD QUESTIONS
# ==========================================

def load_questions():

    questions = []

    with open(
        "questions.csv",
        "r",
        encoding="utf-8"
    ) as f:

        reader = csv.DictReader(f)

        for row in reader:

            questions.append({

                "question": row["question"],

                "options": [

                    row["option1"],
                    row["option2"],
                    row["option3"],
                    row["option4"]

                ],

                "answer": int(
                    row["correct_answer"]
                ) - 1,

                "level": row["level"]
            })

    return questions


# ==========================================
# GET LEVEL QUESTIONS
# ==========================================

def get_level_questions(level):

    questions = load_questions()

    random.shuffle(
        questions
    )

    # QUESTIONS PER LEVEL
    total_questions = 5

    return questions[
        :total_questions
    ]