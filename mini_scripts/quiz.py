print("                             QUIZ!!                              ")
print("-----------------------------------------------------------------")

questions = ("1. Which cartoon character loves eating spinach to gain strength?",
             "2. In Doraemon, which gadget helps Nobita travel anywhere instantly?",
             "3. Which cartoon has characters named Harry, Kulfi, and Gappu Singh",
             )

options = (("A. Tom","B. Popeye","C. Ben 10","D. Shin-chan"),
           ("A. Bamboo Copter","B. Time Machine","C. Anywhere Door","D. Small Light"),
           ("A. Motu Patlu","B. Roll No. 21","C. Pakdam Pakdai","D. Chhota Bheem"))

answers = ("B","C","A")
guesses = []
score = 0
ques_number = 0

for question in questions:
    print("-----------------------------------------------------------------")
    print(question)
    for option in options[ques_number]:
        print(option)
    
    guess = input("Enter your option(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[ques_number]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT!")
        print(f"{answers[ques_number]} is the CORRECT answer")
    ques_number += 1
    
    
print("-----------------------------------------------------------------")
print("                          RESULTS                                ")
print("-----------------------------------------------------------------")

print("Answers: ",end=" ")
for answer in answers:
    for space in range(8):
        print(" ",end=" ")
    print(answer,end=" ")
print()

print("Guesses: ",end=" ")
for guess in guesses:
    for space in range(8):
        print(" ",end=" ")
    print(guess,end=" ")
print()

print("-----------------------------------------------------------------")
print("                          YOUR SCORE                             ")
print("-----------------------------------------------------------------")

# score = int(score / len(questions)* 100)
print(f"Your score: {score} / {len(questions)}")





