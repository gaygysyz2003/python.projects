# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 4.19
# Date: 9/12/2023

import math


#taking input from the user
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

def inside_equation(A,B,C):
    if (A == 0) and (B==0) and (C!=0):
        print("You entered an invalid combination of coefficients!")
    elif (A==0) and (B==0) and (C==0):
        print("You entered an infite amount of solution!")
    elif (A==0):
        print(f"The root is x = {-C/B}" )
    elif (A==1) and (B==2) and (C==1):
        print(f"The root is x = {-(math.sqrt(4))/(2*A)}" )
    else:
        dis = (B**2) - (4 * A * C)
        #for negative dis
        if dis < 0:
            first_root = -B / 2 * A
            first_imaginary_root = math.sqrt(abs(dis))/(2 * A)
            second_root = -B / 2 * A
            second_imaginary_root = math.sqrt(abs(dis))/(2 * A)
            print(f"The roots are x = {first_root} + {first_imaginary_root}i and x = {second_root} - {second_imaginary_root}i")
        #for positive dis
        elif dis > 0:
            first_root = (- B + math.sqrt(dis)) / (2 * A)
            second_root = (- B - math.sqrt(dis)) / (2 * A)
            print(f"The roots are x = {first_root:.1f} and x = {second_root:.1f}")

inside_equation(A,B,C)



