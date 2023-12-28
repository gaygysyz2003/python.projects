# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 6.1
# Date: 9/27/2023 

# iterate from 1 to the input from user

# Input for the left of the "list" will be from (1, n-1)

# Input for the right of the "list" will be (n+1, n+r)

n = int(input("Enter a value for n: "))


def calculate_sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    return result


r = 1

balancing_number = False

while True:
    sum_left = calculate_sum(1, n - 1)
    sum_right = calculate_sum(n + 1, n + r)

    if sum_left == sum_right:
        balancing_number = True
        break

    if sum_left > sum_right:
        r += 1

    if sum_left < sum_right:
        balancing_number = False
        break



if balancing_number:
    print(f'{n} is a balancing number with r={r}')
else:
    print(f'{n} is not a balancing number')







