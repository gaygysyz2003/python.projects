# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 11.12
# Date: 11/09/2023

ym = {'January' : 1,
        'February' : 2,
        'March' : 3,
        'April' : 4,
        'May' : 5,
        'June' : 6,
        'July' : 7,
        'August' : 8,
        'September' : 9,
        'October' : 10,
        'November' : 11,
        'December': 12
        }
import csv

file1 = open('WeatherDataCLL.csv', 'r')
reader = csv.reader(file1, delimiter=',')
maximum = 0
minimum = 100
count = 0
dailytemp = 0
humidtotal = 0
windtotal = 0
precipdays = 0
first_row = True
for row in reader:
    if first_row:
        first_row =  False
        continue
    if row[5] != '':
        temp = int(row[5])
        if temp > maximum:
            maximum = temp
        if row[6] != '':
            temp1 = int(row[6])
            if temp1 < minimum:
                minimum = temp1

print(f'10-year maximum temperature: {maximum} F')
print(f'10-year minimum temperature: {minimum} F')

month = input("Please enter a month: ")
year = input("Please enter a year: ")
file1.seek(0)
first_row = True
for row in reader:
    if first_row:
        first_row = False
        continue
    date = row[0]
    month_num = int(date.split('/')[0])
    year_str = date.split('/')[2]
    if row[4] != '':
        y = int(row[4])
    if month_num == ym[month] and year_str == year:
        count += 1
        dailytemp += y
dailytemp /= count

file1.seek(0)
count = 0
first_row = True
for row in reader:
    if first_row:
        first_row = False
        continue
    date = row[0]
    month_num = int(date.split('/')[0])
    year_str = (date.split('/')[2])
    if row[3] != '':
        humidity = int(row[3])
    if month_num == ym[month] and year_str == year:
        count+=1
        humidtotal += humidity
humidtotal /= count

file1.seek(0)
count = 0
first_row = True 
for row in reader:
    if first_row:
        first_row = False
        continue
    date = row[0]
    month_num = int(date.split('/')[0])
    year_str = date.split('/')[2]
    if row[1] != '':
        windspeed = float(row[1])
    if month_num == ym[month] and year_str == year:
        count +=1
        windtotal += windspeed
windtotal /= count

file1.seek(0)
first_row = True
count = 0
count1 = 0
for row in reader:
    if first_row:
        first_row =  False
        continue
    date = row[0]
    month_num = int(date.split('/')[0])
    year_str = date.split('/')[2]
    if row[2] != '':
        tempp = float(row[2])
    if month_num == ym[month] and year_str == year:
        if tempp == 0:
            count += 1
        elif tempp > 0:
            count += 1
            count1 += 1
precipdays = count1 / count
precipdays *= 100

#finished

print(f'For {month} {year}: ')
print(f'Mean average daily temperature: {dailytemp:.1f} F')
print(f'Mean relative humidity: {humidtotal:.1f}%')
print(f'Mean daily wind speed: {windtotal:.2f} mph')
print(f'Percentage of days with precipitation: {precipdays:.1f}%')