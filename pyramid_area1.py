# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 6.1
# Date: 9/27/2023 


import math

sides = float(input("Enter the side length in meters: "))
num = int(input("Enter the number of layers: "))


#defined a function to solve for area of bottom where (num of layers) x (area of equlateral traingle)
def bottom_equalateral_area(sides, num):
  equalateral_side = sides*num
  calculated_equalateral_area = math.sqrt(3)* equalateral_side * equalateral_side / 4
  return calculated_equalateral_area

#defined a function to solve for walls, the sides of the overall shape
def overall_side_area(sides, num):
  total_sides = 0
  i = 1
  while i<=num:    
    total_sides += i
    i+=1
  area_for_each_side = sides*sides
  calculated_side_area = total_sides * 3 * area_for_each_side
  return calculated_side_area


print(f"You need",round((bottom_equalateral_area(sides, num ) + overall_side_area(sides, num)),2),"m^2 of gold foil to cover the pyramid")

