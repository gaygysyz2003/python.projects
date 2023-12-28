# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 8.00
# Date: 10/16/2023 

#comment everything


user_time = input("Enter the time: ") #input for time 
time_type = input("Choose the clock type (12 or 24): ") # input for clock type 
character = input("Enter your preferred character: ") # input for character
am_pm = ""


char_dict = { #dictionary that pre-formats the values 
  '0': ['...', '. .', '. .', '. .', '...'], 
  '1': [' . ', '.. ', ' . ', ' . ', '...'],
  '2': ['...', '  .', '...', '.  ', '...'],
  '3': ['...', '  .', '...', '  .', '...'],
  '4': ['. .', '. .', '...', '  .', '  .'],
  '5': ['...', '.  ', '...', '  .', '...'],
  '6': ['...', '.  ', '...', '. .', '...'],
  '7': ['...', '  .', '  .', '  .', '  .'],
  '8': ['...', '. .', '...', '. .', '...'],
  '9': ['...', '. .', '...', '  .', '...'],
  'A': [' A  M   M', 'A A MM MM', 'AAA M M M', 'A A M   M', 'A A M   M'],  # use 'A' to print AM
  'P': ['PPP M   M', 'P P MM MM', 'PPP M M M', 'P   M   M', 'P   M   M'],  # use 'P' to print PM
  ':': ['  ', ': ', '  ', ': ', '  ',]
}

while not(character in 'abcdeghkmnopqrsuvwxyz@$&*'): #while loop that checks if the character is appropriate
  print("Character not permitted! ", end='')
  character = input("Try again: ")
print()

user_time = user_time.split(":") # splits the time to get values for the hours and values for the minute 

if (int(user_time[0]) > 24) or (int(user_time[1]) > 60):  # if statement to make sure the hour are in bound
  print("Out of range error")

elif (time_type != '12') and (time_type != '24'): # if statement to make sure the minutes are in bound
  print("Invalid clock type")

else: #if the if and elif statement are not run, this if statement will do changes to the time if the user types in '12' for clock type
  if time_type == "12":
   if int(user_time[0]) >= 12: #if the user has an hour of more than 12 this will make it PM
    am_pm = "P" 
   else:
    am_pm = "A"  #else it is AM
   if (int(user_time[0]) > 12) and (user_time[0] != 24): #if the user's hours is more than 12, it will subtract 12 from the hours 
    user_time[0] = str(int(user_time[0]) - 12)
   if int(user_time[0]) == 0: #if the user's hours is 0, than the hour will be 12
    user_time[0] = "12"

final_time = user_time[0] + ":" + user_time[1] + am_pm #for the final time, combines the hour, minutes, and am_pm

def print_time(time:str, character:str):
  for row in range(5):  # print the first row of each character first then go down 1 row until the last row
    for digit in time:  # put no space in between last number and A or P to get expected output
      char = character
      if char == '':  # if the user does not want a character, use the number being printed
        char = digit
      char_dict[digit][row] = char_dict[digit][row].replace('.', char)
      if (digit == ':') or (digit == time[-1]):  # dont print space if last character in row or is colon
        print(char_dict[digit][row], end='')
      else:
        print(char_dict[digit][row], end=' ')
        char_dict[digit][row] = char_dict[digit][row].replace(char, '.')
    print()

permited_char = 'abcdeghkmnopqrsuvwxyz@$&*=none'

print_time(final_time, character) #the function takes in final_time and character to display the appropriate time