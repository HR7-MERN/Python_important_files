print("Hi! Welcome to my computer quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Let's play the online quiz :)")
score = 0
answer = input("What is the fullform of ATM? ")
if answer.lower() == "automated teller machine":
    print("correct!")
    score += 1
else:
    print("Incorrect")
answer = input("What is the full form of CFI? ")
if answer.lower() == "customer identification file":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What is the full form of KYC? ")
if answer.lower() == "know your customer":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What is the full form of GCC? ")
if answer.lower() == "green channel counter":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What is the full form of CSP? ")
if answer.lower() == "customer service point":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
print("You got " + str(score) + " answers correct!")
print("You scored " + str((score/5)*100) + "%.")
print("You are a champion!")
