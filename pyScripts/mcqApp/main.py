from Question import Question
question_Structure = [
    "What is 5+5 ? \n (a) 12\n (b) 10\n (c) 14\n\n",
    "What is 15+5 ? \n (a) 20\n (b) 10\n (c) 14\n\n",
    "What is 25+5 ? \n (a) 12\n (b) 30\n (c) 14\n\n"
]

# LIST OF OBJECTS FOR THE CLASS, assiging the question and the correct answer
questions = [
    Question(question_Structure[0], "b"),
    Question(question_Structure[1], "a"),
    Question(question_Structure[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        
        # questoin.prompt is coming from the class Question 
        usrAns = input(f"{question.prompt} \n Your answer: ")
        
        # questoin.answer is coming from the class Question 
        if usrAns == question.answer:
            score+=1
    print(f"You got {score}/{len(questions)} correct")
run_test(questions)