# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 8.00
# Date: 10/16/2023 

#### Kevin ####
while not(character in 'abcdeghkmnopqrsuvwxyz@$&*'): #while loop that checks if the character is appropriate
  print("Character not permitted! ", end='')
  character = input("Try again: ")


if (int(user_time[0]) > 24) or (int(user_time[1]) > 60):  # if statement to make sure the hour are in bound
  print("Out of range error")

elif (time_type != '12') and (time_type != '24'): # if statement to make sure the minutes are in bound
  print("Invalid clock type")

final_time = user_time[0] + ":" + user_time[1] + am_pm #for the final time, combines the hour, minutes, and am_pm