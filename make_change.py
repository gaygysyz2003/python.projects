# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 4.13
# Date: 9/11/2023

# input from the user

user_paid = float(input("How much did you pay? "))
user_costed = float(input("How much did it cost? "))

#calculate the user charge

change = user_paid - user_costed
change_cents = change * 100

#calculate the number of quarters, dimes, and pennies
quarters_left = change_cents // 25
change_cents %= 25


dimes_left = change_cents // 10
change_cents %= 10


nickels_left = change_cents // 5
change_cents %= 5

change_cents = round(change_cents, 3)
pennies = change_cents  #fix this shit





#output the changes
print(f'You received $ {change:.2f} in change. That is... ')

#quarter plurals go crazy with this code
if (quarters_left > 0) and (quarters_left < 2):
        print(f"{int(quarters_left)} quarter")
elif (quarters_left >=2):
    print(f"{int(quarters_left)} quarters")
else:
    quarters_left = 0

#dime plurals go crazy with this code
if (dimes_left > 0) and (dimes_left < 2):
    print(f"{int(dimes_left)} dime")
elif (dimes_left>=2):
    print(f"{int(dimes_left)} dimes")
else:
    quarters_left = 0

#nickle plurals go crazy with this code
if (nickels_left > 0) and (nickels_left < 2):
    print(f"{int(nickels_left)} nickel")
elif (nickels_left>=2):
    print(f"{int(nickels_left)} nickels")
else:
    nickels_left = 0

#penny plurals go crazy with this code
if (pennies == 1):
     print(f'{int(pennies)} penny')
elif (pennies > 1):
     print(f'{int(pennies)} pennies')
else:
    pennies = 0