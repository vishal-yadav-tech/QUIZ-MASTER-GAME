import csv
import os

LEADERBOARD_FILE = "leaderboard.csv"


# ==========================================
# SAVE SCORE
# ==========================================

def save_score(name, score):

    file_exists = os.path.isfile(
        LEADERBOARD_FILE
    )

    with open(

        LEADERBOARD_FILE,

        "a",

        newline="",

        encoding="utf-8"

    ) as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow([
                "name",
                "score"
            ])

        writer.writerow([
            name,
            score
        ])


# ==========================================
# LOAD SCORES
# ==========================================

def load_scores():

    scores = []

    if not os.path.exists(
        LEADERBOARD_FILE
    ):

        return scores

    with open(

        LEADERBOARD_FILE,

        "r",

        encoding="utf-8"

    ) as f:

        reader = csv.DictReader(f)

        for row in reader:

            scores.append({

                "name":
                row["name"],

                "score":
                int(row["score"])
            })

    scores.sort(

        key=lambda x: x["score"],

        reverse=True
    )

    return scores[:10]