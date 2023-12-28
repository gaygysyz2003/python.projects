# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 4.15
# Date: 10/30/2023
def is_empty(s):
    return len(s) == 0

def from_roman(roman_numeral):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
   
    if is_empty(roman_numeral):
        return 0

    decimal_value = 0
    prev_value = 0

    for symbol in reversed(roman_numeral):
        current_value = symbols[symbol]
        if current_value < prev_value:
            decimal_value -= current_value
        else:
            decimal_value += current_value
        prev_value = current_value

    return decimal_value

def compare_roman_numerals(roman_numeral_1, roman_numeral_2):
    a = from_roman(roman_numeral_1)
    b = from_roman(roman_numeral_2)
    if a < b:
        return -1
    if a == b:
        return 0
    return 1
   
def main():
    num1 = input("Enter the first Roman numeral: ")
    num2 = input("Enter the second Roman numeral: ")
    result = compare_roman_numerals(num1, num2)
    if result == -1:
        compare = 'smaller than'
    elif result == 0:
        compare = 'equal to'
    else:
        compare = 'larger than'
    print(f'{num1} is {compare} {num2}')
   
if __name__ == '__main__':
    main()