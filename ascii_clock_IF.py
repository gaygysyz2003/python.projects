# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 8.00
# Date: 10/16/2023 

### IAN ### 
def print_time(time:str, character:str):
  for row in range(5):  # print the first row of each character first then go down 1 row until the last row
    for digit in time:  # put no space in between last number and A or P to get expected output
      char = character
      if char == 'none':  # if the user does not want a character, use the number being printed
        char = digit
      char_dict[digit][row] = char_dict[digit][row].replace('.', char)
      if (digit == ':') or (digit == time[-1]):  # dont print space if last character in row or is colon
        print(char_dict[digit][row], end='')
      else:
        print(char_dict[digit][row], end=' ')
        char_dict[digit][row] = char_dict[digit][row].replace(char, '.')
    print()
