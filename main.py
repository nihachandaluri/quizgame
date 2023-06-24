questions = ("Entomology is the science that studies ?: ",
             "What is part of a database that holds only one type of information?:",
             "OS computer abbreviation usually means ?:",
             "'.MOV' extension refers usually to what kind of file?:",
             "In which decade with the first transatlantic radio broadcast occur?:")

options = (("A.Behavior of human beings","B.Insects","C.The origin and history of technical and scientific terms","D.The formation of rocks"),
           ("A.Report","B.field","C.record","D.file"),
           ("A.Order of significance","B.Open software","C.Operating system","D.Optical sensor"),
           ("A.Image file","B.Animation/movie file","C.Audio file","D.Ms office document"),
           ("A.1850s","B.1860s","C.1870s","D.1900s"))

answers = ("B","B","C","B","D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-------------------------")    
print("        RESULTS          ")
print("-------------------------")

print("answers:",end="")
for answer in answers:
    print(answer,end="")
print()

print("guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is:{score}%")
