# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 4.15
# Date: 10/30/2023

def list_nums(integers):
    # Create a list to store the four numbers
    numbers = []

    # Start with the largest possible number (sqrt(n)) and work backward
    a = int(integers ** 0.5)

    while a > 0:
        # Find the remaining sum
        remaining_sum = integers - a * a

        # Try to find three squares that sum up to the remaining sum
        b = int(remaining_sum ** 0.5)
        while b >= 0:
            # Find the remaining remaining sum
            remaining_remaining_sum = remaining_sum - b * b

            # Try to find two squares that sum up to the remaining remaining sum
            c = int(remaining_remaining_sum ** 0.5)
            while c >= 0:
                # Find the fourth number
                d = int((remaining_remaining_sum - c * c) ** 0.5)

                # Check if the four numbers' squares add up to the original number
                if a * a + b * b + c * c + d * d == integers:
                    numbers = [a, b, c, d]
                    return numbers

                c -= 1
            b -= 1
        a -= 1

    return numbers


