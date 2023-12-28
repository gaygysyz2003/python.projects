# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 6.15
# Date: 9/27/2023 
import math

user_entered = int(input("Enter a positive integer: "))

a1 = user_entered

# if input is even, I will take square root of the number user entered

# if input is odd, I will 3/2 power what user entered

i = 0

sequence = str(user_entered) + ", " + ""

if(user_entered == 1):
    sequence = str(user_entered)

while (user_entered != 1):
    if(user_entered % 2 == 1): # this means it's odd
        user_entered = math.floor(math.pow(user_entered, 3/2))
    elif(user_entered % 2 == 0): #this means it's even
        user_entered = math.floor(math.sqrt(user_entered))
    if (user_entered == 1):
        sequence += str(user_entered)
    else:
        sequence += str(user_entered) + ", "

    i += 1

print(f'The Juggler sequence starting at {a1} is: \n{sequence} \nIt took {i} iterations to reach 1')

