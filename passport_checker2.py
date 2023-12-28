# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 9:15
# Date: 10/23/2023

#initiate the variables
file_Name = input("Enter the name of the file: ")
file1 = open(file_Name, "r")
file2 = open("valid_passports2.txt", "w")
num_valid_people = 0
valid_data = []
people_data = []
code = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "pid:", "cid:"]
certain_char = "0123456789abcdef"

#the function that will be used 
def check(line):
    if("hgt" in line[0]):
        if "in" in line[1]:  
            temp = int(line[1].split("in")[0])
            if (not(int(temp) >= 59 and int(temp) <= 76)):
                return False
        elif "cm" in line[1]:
            temp = int(line[1].split("cm")[0])
            if (not(int(temp) >= 150 and int(temp) <= 193)):
                return False
        else:
            return False
    if("byr" in line[0]):
        if not(len(line[1]) == 4) or not(1920 <= int(line[1]) <= 2007):
            return False
    if("eyr" in line[0]):
        if not(len(line[1]) == 4) or not(2023 <= int(line[1]) <= 2033):
            return False
    if("iyr" in line[0]):
        if not(len(line[1]) == 4) or not(2013 <= int(line[1]) <= 2023):
            return False
    if("hcl" in line[0]):
        if not(len(line[1][1:]) == 6) or not(line[1][0] == "#"):
            return False
        c = 0
        for i in range(1, len(line[1])):
            if line[1][i] in certain_char:
              c += 1
        if c != 6:
          return False;
    if("pid" in line[0]):
        if not(len(str(line[1])) == 9):
            return False
    if("cid" in line[0]):
        if not(len(line[1]) == 3) or not(int(line[1]) >= 100 and int(line[1]) < 1000):
            return False
    return True

for line in file1:
    people_data.append(line)
    if line == "\n":
        p = "".join(people_data)
        checker = True
        for i in code:
            if not(i in p):
                checker = False
        tP = p.replace("\n", " ")
        split_tP = tP.split()
        for l in split_tP:
            l = l.split(":")
            checker = check(l)
            if(not checker):
                checker = False
                break;
        
        for i in code:
            if not(i in p):
                checker = False
        
        if checker:
            num_valid_people += 1
            valid_data.append(p)
        people_data = []

p = "".join(people_data)
checker = True

for i in code:
    if not(i in p):
        checker = False

tP = p.replace("\n", " ")
split_tP = tP.split()

for l in split_tP:
    l = l.split(":")
    checker = check(l)
    if(not checker):
        checker = False
        break;

for i in code:
    if not(i in p):
        checker = False

if checker:
    num_valid_people += 1
    valid_data.append(p)


for x in valid_data:
    file2.write(x)

print(f"There are {num_valid_people} valid passports")

file2.close()
file1.close()

