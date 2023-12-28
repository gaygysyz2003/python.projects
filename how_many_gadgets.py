# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 4.18
# Date: 9/12/2023

#get input from the user
days = int(input("Please enter a positive value for day: "))
num_gadget = 0

#created a function for this for calculations
def gadgets(day,num):
    num_gadget = day * num
    return num_gadget

if days < 0:
    print("You entered an invalid number!")
    
else:
    if days <= 10:
        num_gadget = (10 * days)
        print(f'The sum total number of gadgets produced on day {days} is {num_gadget}')
    elif(10 < days < 50):
        num_gadget = int(45 + (1/2) * (days ** 2 + days))
        print(f'The sum total number of gadgets produced on day {days} is {num_gadget}')
    elif(50 < days <= 100):
        num_gadget = 1320 + (days - 50) * 50
        print(f'The sum total number of gadgets produced on day {days} is {num_gadget}')
    else:
        num_gadget = 3820
        print(f'The sum total number of gadgets produced on day {days} is {num_gadget}')
