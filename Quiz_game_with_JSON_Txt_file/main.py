import json

def load_quiz_data():
    with open("quiz.json", "r") as file:
        quiz_data = json.load(file)
    return quiz_data

def display_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")

def check_answer(user_answer, question_data):
    correct_answer = question_data["answer"]
    return user_answer == correct_answer

def play_quiz(quiz_data):
    score = 0
    num_questions = len(quiz_data["questions"])

    for question in quiz_data["questions"]:
        display_question(question)
        user_answer = input("Your Answer: ").upper()

        if check_answer(user_answer, question):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    #final_score = int((score / num_questions) * 100)
    #print(f"\nQuiz Completed! Your Final Score: {final_score}%")

    print(f"Final score: {score} / {len(question)}".center(10))

def main():
    print("Quiz Game")
    print("----------")
    print("1. Start Quiz")
    print("2. Exit")
    choice = input("Enter your Choice: ")

    while choice == "1":
        print("Quiz Loaded!")
        print("----------")
        quiz_data = load_quiz_data()
        play_quiz(quiz_data)

        print("\n1. Retry Quiz")
        print("2. Exit")
        choice = input("Enter your Choice: ")

    print("\nExiting...")

if __name__ == "__main__":
    main()
