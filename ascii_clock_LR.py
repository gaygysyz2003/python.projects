# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 8.00
# Date: 10/16/2023 

########LUKE#########
user_time = input("Enter the time: ")
time_type = input("Choose the clock type (12 or 24): ")
character = input("Enter your preferred character: ")
am_pm = 0

user_time = user_time.split(":")
if time_type == "12":
  if int(user_time[0]) > 12:
    user_time[0] = str(int(user_time[0]) - 12)
    am_pm = "pm"
  else:
    am_pm = "am" 

elif time_type == "24":
  continue
