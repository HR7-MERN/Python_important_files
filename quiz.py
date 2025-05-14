print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

score = 0

if playing.lower() != "yes":
    quit()
print("Okay! Let's play the quiz :)")

answer = input("1. What does cpu stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Oops that's an Incorrect answer :(")
    print("The correct answer is: central processing unit")

answer = input("2. What does Gpu stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Oops that's an Incorrect answer :(")
    print("The correct answer is: graphics processing unit")

answer = input("3. What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Oops that's an Incorrect answer :(")
    print("The correct answer is: random access memory")

answer = input("4. What does psu stands for? ")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print("Oops that's an Incorrect answer :(")
    print("The correct answer is: power supply unit")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")
