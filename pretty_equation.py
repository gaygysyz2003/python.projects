# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 4.17
# Date: 9/14/2023

#taking the user input
#make all the variables for this equation
import math
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

solution = ""

def c_A(A):
    solution = ""
    if(A == 1):
        solution += "x^2"
    elif(A == -1):
        solution += "- " + "x^2"
    elif(A < 0):
        solution += ("- " + str(abs(A)) + "x^2")
    elif(A > 0):
        solution += (str(abs(A)) + "x^2")
    else:
        solution = ""
    return solution


if(A == 0):
    if(B == 1):
        solution += ("x ")
    elif(B < 0):
        solution += ("- " + str(abs(B)) + "x ")
    elif(B > 0):
        solution += (str(abs(B)) + "x ")

def c_B(B):
    solution = ""
    if(B == 1):
        solution += ("+ " + "x")
    elif(B == -1):
        solution += ("- " + "x")
    elif(B < 0):
        solution += "- " + str(abs(B)) + "x"
    elif(B > 0):
        solution += "+ " + str(abs(B)) + "x"
    return solution

def c_C(C):
    solution = ""
    if(C < 0):
        solution += " - " + str(abs(C))
    elif(C > 0):
        solution += "+ " + str(abs(C))
    return solution


if (A == 0):
    solution += c_A(A) + c_C(C)
elif(B == 0):
    solution += c_A(A) + c_C(C)
elif(C == 0):
    solution += c_A(A) + " " + c_B(B)
elif((C == 0) and (B == 0)):
    solution += c_A(A)
else:
    solution += c_A(A) + " " + c_B(B) + " " + c_C(C)


print(f'The quadratic equation is {solution} = 0')