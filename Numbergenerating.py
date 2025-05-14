# random is a python module by default, and it gives a random number from the selected range of numbers.
import random
# We are going to print a random number and user can guess the random number
# We will show the user whether they are above the number or below the number while guessing the numbers.
# Here we are going to crate a charecter and ask the use to type a number which is >0.
top_of_range = input("Please type a number: ")
# We have assigned the variable,  now we need to conver the user input to an integer.
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    # Here we need to check if the input is a string or an integet and if it is a number and then it will be converted to an integer. Otherwise, the we will ask the uer to type a number > 0.
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        # quit is used to quit the condition and the user needs to start it from the begining.
        quit()
else:
    print("Please type a number next time")
    quit()

# We have converted the top_of_range to an integer and now we will print the random numbers from the top_of_range
random_number = random.randint(0, top_of_range)
while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
