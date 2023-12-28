# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 4.15
# Date: 11/1/2023

#defined the message user will receive 
def check(guess):
    if int(guess) > 27:
        print("Too high!")
    elif int(guess) < 27:
        print("Too low!")
    else:
        print(won())

def won():
    return f"You guessed it! It took you {attempted} guesses."

print("Guess the secret number! Hint: it's an integer between 1 and 100... ")

#variables 
attempted = 0
guessed = 0
secret_num = 27

while guessed != secret_num:
    attempted += 1
    guessed = input("What is your guess? ")
    keep = True

    while keep == True:

        try:
            check(guessed)
            break

        except:
            guessed = input("Bad input! Try again: ")
            continue

    if guessed == str(secret_num):
        break
    






        



     

    







#try and except that will display the input until it's right

#counts up how many times the user missed and displays at the end

#let's the user know if he is too high/ or low

#displays error message if the input is not integer

#while loop that will repeat this step until user enterance is 27