# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 6.14
# Date: 9/27/2023
import math

#this is the function for doublefactorial
def doublefactorial(num):
    if num <=0 :#it just prints 1 if the number equals 1
        return 1
    elif num ==1:
        return 1
    
    elif num == 2:
        return 2

    elif num % 2 == 0:
        out=num
        for i in range(num-2 , 1, -2):
            out *= i 
        return out
    elif num % 2!= 0:
        for i in range(num-2 , 1, -2):
            num *= i
        return num


print(doublefactorial(6))
    
    
    






