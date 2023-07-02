print( "Quiz Game")
print ( "---------- ")
print("1. Start Quiz.\n2. Exit.\nEnter your Choice: ")
user = input()
while user == "1" :
    print("Quiz Loaded!")
    print ( "---------- ")

    questions = ("\nQuestion 1 : \n\nWhat is the capital of France?: ", 
                        "\nQuestion 2 : \n\nWhich planet is known as the Red Planet?: ",
                        "\nQuestion 3 : \n\nWhat is the largest ocean on Earth?:  ")

    options = (("A. Paris", "B. London", "C. Rome", "D. Madrid"),
                    ("A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"),
                    ("A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"))

    answers = ("A", "A", "C")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("\nYour Answer : ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("\nCORRECT!")
        else:
            print("\nINCORRECT!")
            
        question_num += 1


    print("      \nQuiz Completed!        ")
    print("----------------------")



    score = int(score / len(questions) * 3)
    print(f"\nFinal score : {score}/3")
    
    print("\n1. Retry Quiz.\n2. Exit.\nEnter your Choice: ")
    user = input()


else: 
    print("\nExiting.....")
