# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 9:15
# Date: 10/23/2023

fileName = input("Enter the name of the file: ")
file1 = open(fileName, "r")
file2 = open("valid_passports.txt", "w")

num_valid_people = 0
valid_data = []
people_data = []
code = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "pid:", "cid:"]

for line in file1:
    people_data.append(line)
    if line == "\n":
        p = "".join(people_data)
        checker = True
        for i in code:
            if not(i in p):
                checker = False
        if checker:
            num_valid_people += 1
            valid_data.append(p)
        people_data = []


#add all in people into one string
p = "".join(people_data)
checker = True

for i in code:
    if not(i in p):
        checker = False
if checker:
    valid_data.append(p)
    num_valid_people += 1

for x in valid_data:
    file2.write(x)

print(f"There are {num_valid_people} valid passports")

file2.close()
file1.close()





