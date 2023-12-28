# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 11.12
# Date: 11/09/2023

#pixel_triangle.csv
file = input("Enter the filename: ")
new_file = file[:-3]
new_file = new_file + "txt"
character = input("Enter a character: ")

opened = open(file, "r")
wrote = open(new_file, "w")

for i in opened:
    list_a = []
    list_a_int = []
    i = i.strip()
    counter = 0
    list_a = i.split(',')
    for numbers in list_a:
        list_a_int.append(int(numbers))
    for num in list_a_int:
        if counter % 2 == 0:
            wrote.write(' '*num)
            counter += 1
        else:
            wrote.write(character*num)
            counter += 1
    wrote.write('\n')

opened.close()
wrote.close()
print(f'{new_file} created!')






