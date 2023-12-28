# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 5.4
# Date: 9/18/2023

import math
# get input from the user

user_input = float(input("Enter the excess temperature: "))
#testing if the input is in the range
if user_input < 1.3 or user_input > 1200:
    print(f"Surface heat flux is not available")
    #if not this code will stop running
    exit()
else: #by this point the input is in the range so now we are checking if it's inside the 1.3 and 5
    if (user_input > 1.3) and (user_input < 5):
        m = math.log(7000/1000) / math.log( 5 / 1.3)
        calculated = 1000*(user_input /1.3)** m
    # if the code has gotten here then the number is larger than 5 and it's going to check if it's less than 30
    elif(user_input > 5) and (user_input < 30):
        m = math.log(1.5 * (10**6) / 7000) / math.log(30 / 5)
        calculated = 7000*(user_input /5)** m
    # the code is greater than 30!
    elif (user_input > 30) and (user_input < 120):
        m = math.log((2.5 * (10**4)) / (1.5 * (10**6))) / math.log(120 / 30)
        calculated = (1.5 * (10**6)) * (user_input /30)** m
    #this the last line of code and this is the only choice for the calculations to be done
    elif (user_input > 120) and (user_input < 1200):
        m = math.log((1.5 * (10**6))/ (2.5 * (10**4))) / math.log(1200 / 120)
        calculated = (2.5 * (10**4)) * (user_input /120)** m
    #this code works to make everything simple by first checking for where the input belongs for the calculation so that we don't have to move around but instead build up my code like how egyptians built pyrmaids.


# this is the last code that will print out the output by rounding it.
print(f"The surface heat flux is approximately {round(calculated)} W/m^2")lab 