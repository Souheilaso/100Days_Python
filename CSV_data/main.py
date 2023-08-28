# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data)
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)

# import statistics
# print(statistics.mean(temp_list))
#

average = data["temp"].mean()
print(average)
