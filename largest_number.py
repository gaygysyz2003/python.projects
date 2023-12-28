# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 4.16
# Date: 9/11/2023
# let them enter a number x, y, z
x=float(input("Enter number 1:"))
y=float(input("Enter number 2:"))
z=float(input("Enter number 3:"))

#these will check which one has higher number
if((x>y)and(x>z)):
	max_num=x
elif((y>z)and(y>x)):
	max_num=y
else:
	max_num=z
print("The largest number is",max_num)