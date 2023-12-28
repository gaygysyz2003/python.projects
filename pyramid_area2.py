# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 6.12
# Date: 9/27/2023 


import math
#user enters number of sides and length
sides = float(input("Enter the side length in meters: "))
num = int(input("Enter the number of layers: "))


# Defined a function to solve for the area of the bottom (base) of the pyramid
def bottom_equilateral_area(sides, num):
   equilateral_side = sides * num
   calculated_equilateral_area = math.sqrt(3) * equilateral_side * equilateral_side / 4
   return calculated_equilateral_area


# Defined a function to solve for the area of the sides of the overall shape
def overall_side_area(sides, num):
   # Calculate the total number of sides in the overall shape
   total_sides = num * (num + 1) // 2
   area_for_each_side = sides * sides
   calculated_side_area = total_sides * 3 * area_for_each_side
   return calculated_side_area


# Calculate and print the total area needed
total_area = bottom_equilateral_area(sides, num) + overall_side_area(sides, num)
print(f"You need {total_area:.2f} m^2 of gold foil to cover the pyramid")
