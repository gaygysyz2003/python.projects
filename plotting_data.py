# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 12.12
# Date: 11/18/2023


import matplotlib.pyplot as plt
high_temp_list = []
low_temp_list = []
avg_temp_list = []

date_list = []
wind_list = []
precipitation_list = []
humidity_list = []

month_list = []
month_avg_temperature_list = []
month_high_temperature_list = []
month_low_temperature_list = []

with open('WeatherDataCLL.csv', 'r+') as weather:
    for line in weather:
        line = line.strip().split(',')
        if line[0] == 'Date':
            continue

        # Date / Wind
        date = line[0].split('/')
        wind = line[1]
        if wind == '':
            wind_list.append(7.5)
        else:
            wind_list.append(float(wind))
        date_list.append(int(date[2]))

        # MINIMUM TEMPERATURE
        temperature_min = line[6]
        if temperature_min == '':
            low_temp_list.append(50)
        else:
            low_temp_list.append(int(temperature_min))

        # MAXIMUM TEMPERATURE
        temperature_max = line[5]
        if temperature_max == '':
            high_temp_list.append(90)
        else:
            high_temp_list.append(int(temperature_max))


        # PRECIPITATION
        precipitation = line[2]
        if precipitation == '':
            precipitation_list.append(5)
        else:
            precipitation_list.append(float(precipitation))

        # HUMIDITY
        humidity = line[3]
        if humidity == '':
            humidity_list.append(80)
        else:
            humidity_list.append(int(humidity))


        # Average temperature
        month = date[0]
        month_list.append(int(month))
        avg_temperature = line[4]
        if avg_temperature == '':
            avg_temp_list.append(75)
        else:
            avg_temp_list.append(int(avg_temperature))






# APPENDS EACH TEMPERATURE INTO DESIGNATED LIST
for i in range(len(month_list)):
    month_avg_temperature_list.append((month_list[i], avg_temp_list[i]))



for j in range(len(month_list)):
    month_high_temperature_list.append((month_list[j], high_temp_list[j]))


for k in range(len(month_list)):
    month_low_temperature_list.append((month_list[k], low_temp_list[k]))







# DICTIONARIES TO ORGANIZE MONTHS AND TEMPERATURES
avg_temps = {}

for month, temperature in month_avg_temperature_list:
    if month in avg_temps:
        avg_temps[month].append(temperature)
    else:
        avg_temps[month] = [temperature]

avg_high_temps = {}



for month, temperature in month_high_temperature_list:
    if month in avg_high_temps:
        avg_high_temps[month].append(temperature)
    else:
        avg_high_temps[month] = [temperature]



avg_low_temps = {}

for month, temperature in month_low_temperature_list:
    if month in avg_low_temps:
        avg_low_temps[month].append(temperature)
    else:
        avg_low_temps[month] = [temperature]



# APPEND AVERAGE OF THE AVG TEMPERATURES IN EACH MONTH
avg_result = []


for month, temperatures in avg_temps.items():
    avg_result.append((month, sum(temperatures) / len(temperatures)))


# APPEND MAX OF AVG HIGH TEMPERATURES IN EACH MONTH
max_result = []

for month, temperatures in avg_high_temps.items():
    max_result.append((month, max(temperatures)))



# APPEND MIN OF AVG LOW TEMPERATURES IN EACH MONTH
min_result = []

for month, temperatures in avg_low_temps.items():
    min_result.append((month, min(temperatures)))


# print(f'Min result: {min_result}')  # TEST CASES
#
# print(f'Max result: {max_result}')  # TEST CASES
#
# print(f'Avg result: {avg_result}')  # TEST CASES


def temp_by_month():
    month_temp = []
    max = []
    min = []
    avg = []

    # MONTH FOR PLOTTING
    for i in range(len(min_result)):
        month_temp.append(min_result[i][0])

    # MAX FOR PLOTTING
    for j in range(len(max_result)):
        max.append(max_result[j][1])

    # MIN FOR PLOTTING
    for k in range(len(min_result)):
        min.append(min_result[k][1])

    # AVG FOR PLOTTING
    for l in range(len(avg_result)):
        avg.append(avg_result[l][1])

    plt.figure()
    plt.title('Temperature by Month')
    plt.plot(month_temp, max, color='red', label = 'High T')
    plt.plot(month_temp, min, color='blue', label = 'Low T')

    plt.bar(month_temp, avg, color='khaki')
    plt.xlabel('Month')
    plt.ylabel('Average Temperature, F')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plt.legend()
    plt.show()


def humidity_vs_precipitation():
    plt.scatter(humidity_list, precipitation_list, color='black', s=10)
    plt.title('Precipitation vs Average Relative Humidity')
    plt.ylabel('Precipitation (in)')
    plt.xlabel('Average Relative Humidity (%)')
    plt.show()




def wind_days_count(list):
    result = []
    for i in wind_list:
        for index, item in enumerate(result):
            if item[1] == i:
                result[index] = (item[0] + 1, i)
                break
        else:
            # This block is executed if the loop completes without a break
            result.append((1, i))

    print(result)

    days = []
    wind_elements = []

    for i in range(len(result)):
        days.append(result[i][0])

    for j in range(len(result)):
        wind_elements.append(result[j][1])


    plt.figure()
    plt.bar(wind_elements, days, color='green', edgecolor = 'black', linewidth=1)
    plt.title('Histogram of Average Wind Speed')
    plt.ylabel('Number of days')
    plt.xlabel('Average Wind Speed, mph')
    plt.xticks([0.0, 2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0])
    plt.show()


# MORE TEST CASES
# print(temp_list)
# print(date_list)
# print(wind_list)

def linear_plot():
    fig, ax1 = plt.subplots()

    ax1.plot(high_temp_list, color = 'r', label = 'Max Temperature')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Maximum Temperature, F')
    ax1.legend(loc = 'lower left')

    ax2 = ax1.twinx()
    ax2.plot(wind_list, color='b', label='Average Wind Speed')
    ax2.set_ylabel('Average Wind Speed, mph')
    ax2.set_yticks([2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0])
    ax2.legend(loc = 'lower right')


    plt.title('Maximum Temperature and Average Wind Speed')
    plt.show()








linear_plot()
wind_days_count(wind_list)
humidity_vs_precipitation()
temp_by_month()
 



# #"Date"
# #"Maximum Temperature "
# #"Average Wind Speed"


