print( "Quiz Game")
print ( "---------- ")
print("1. Start Quiz.\n2. Exit.\nEnter your Choice: ")
user = input()
while user == "1" :
 print("Quiz Loaded!")
 print ( "---------- ")


 with open('questions.txt' , 'r') as quesfile, open('options.txt','r') as optionfile, open('answers.txt','r') as ansfile:
    questions = [question.strip() for question in quesfile.readlines()]
    options = [option.strip() for option in optionfile.readlines()]
    answers = [answer.strip() for answer in ansfile.readlines()]
    
    guesses = []
    score = 0
    question_num = 0


    for question in questions:
        
        print(question)
        for option in options[question_num]:
            print(option, end="")

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

    print(f"Final score: {score} / {len(questions)}".center(10))

    
    print("\n1. Retry Quiz.\n2. Exit.\nEnter your Choice: ")
    user = input()

else: 
    print("\nExiting.....")
