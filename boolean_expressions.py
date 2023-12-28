# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 4.15
# Date: 9/12/2023

############ Part A ############
# Input Boolean values from the keyboard
first_input = input("Enter True or False for a: ")
second_input = input("Enter True or False for b: ")
third_input = input("Enter True or False for c: ")


# Convert user input to Boolean values
first_input = first_input.lower() in ['true', 't']
second_input = second_input.lower() in ['true', 't']
third_input = third_input.lower() in ['true', 't']

############ Part B ############
# Evaluate Boolean expressions
expr1 = first_input and second_input and third_input
expr2 = first_input or second_input or third_input

print("a and b and c: ", expr1)
print("a or b or c:  ", expr2)

############ Part C ############
# Construct and evaluate Boolean expressions
expr3 = (first_input or second_input) and not (first_input and second_input)
expr4 = (first_input + second_input + third_input) in [1, 3]

print("XOR: ", expr3)
print("Odd number: ", expr4)
