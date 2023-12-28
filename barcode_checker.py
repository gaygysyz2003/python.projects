# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 11.11
# Date: 10/23/2023

#assign group 2 to second half

#for the first group sum all of the numbers up

#for the second group sum all of the numbers up

#multiply second group by 3

#add second group with first group

#pick the last digit of the answer and subtract the answer from 10

#compare it with the last digit in the file, if it matches then it is valid and add it to valid barcode.txt

#print out the total number of valid barcodes


# function check_barcode() to check if an input barcode is valid or not
def check_barcode(str1):
    # set sum of first group to 0
    first_group = 0
    # set sum of second group to 0
    second_group = 0
    # loop the string and find the sum of first group
    for i in range(0, len(str1)-1, 2):
        first_group = first_group + int(str1[i])

    # loop the string and find the sum of second group
    for i in range(1, len(str1)-1, 2):
        second_group = second_group + int(str1[i])

    # multiply second group by 3
    second_group = second_group * 3
    # add first group and second group
    new_num = first_group + second_group
    # get the last digit and subtract from 10
    last_digit = 10 - (new_num % 10)
    # if it is equal to last digit of input barcode, then it is valid otherwise it is invalid.
    if (last_digit == int(str1[-1])):
        return True
    else:
        return False

if __name__ == '__main__':
    # take file name as input
    filename = input("Enter the name of the file: ")
    # set an empty list to store valid barcode list
    valid_barcode_list = []
    # open the file
    with open(filename) as data:
        # read all barcodes and store in a list
        all_barcode = data.readlines()
        # loop through all barcode of the list
        for code in all_barcode:
            # remove any extra characters
            code = code.strip()
            # call the function check_barcode() and check if the bar code is valid or not
            if (check_barcode(code) == True):
                # if it is valid then append the barcode to the list valid_barcode_list
                valid_barcode_list.append(code)

    # open file valid_barcodes.txt and write all valid barcodes in it
    with open("valid_barcodes.txt", 'w') as f:
        for code in valid_barcode_list:
            f.write(code)
            f.write("\n")

    # print total number of valid barcodes
    print(f"There are {len(valid_barcode_list)} valid barcodes") 
        
            
        