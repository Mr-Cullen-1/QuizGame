import sys
sys.stdout.reconfigure(encoding='utf-8')


questions = [
    {
        "prompt":"What is the result of 5 * 3 + 2?",
        "options": ["A. 17", "B. 21", "C. 15", "D. 19"],
        "answer":"A"
    },
    {
        "prompt":"What is the only mammal capable of true flight?",
        "options":["A. Squirrel", "B. Bat", "C. Kangaroo", "D. Penguin"],
        "answer":"B"
    },
    {
        "prompt":"Which country has the shape of a boot?",
        "options":["A. Spain", "B. France", "C. Portugal", "D. Italy"],
        "answer":"D"
    },
    {
        "prompt":"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
        "options":["A. Echo", "B. Shadow", "C. Whisper", "D. Breeze"],
        "answer":"A"
    },
    {
        "prompt":"In which movie does a character say, \"I\'m the king of the world\"?",
        "options":["A. The Lion King", "B. Titanic", "C. Frozen", "D. Avatar"],
        "answer":"B"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C or D): ").upper()
        if answer == question["answer"]:
            print("Correct answer! \n")
            score += 1
        else:
            print("Incorrect answer, correct answer is", question["answer"], "\n")
    print("You got", score, "out of", len(questions), "correct.")

run_quiz(questions)