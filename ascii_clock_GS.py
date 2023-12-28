# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 8.00
# Date: 10/16/2023 

char_dict = {
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
  'A': ['  A   M   M', ' A A  MM MM', 'AAAAA M M M', 'A   A M   M', 'A   A M   M'],  # use 'A' to print AM
  'P': ['PPP M   M', 'P P MM MM', 'PPP M M M', 'P   M   M', 'P   M   M'],  # use 'P' to print PM
  ':': ['   ', ' : ', '   ', ' : ', '   ',]
}
permited_char = 'abcdeghkmnopqrsuvwxyz@$&*=none'

# function with an input string of time   
#ex: time - '11:27A'
# output:
# .   .      ... ...   A   M   M 
#..  ..   :    .   .  A A  MM MM 
# .   .      ...   . AAAAA M M M 
# .   .   :  .     . A   A M   M 
#... ...     ...   . A   A M   M 
