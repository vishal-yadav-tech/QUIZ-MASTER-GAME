import csv


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