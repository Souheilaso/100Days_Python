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

# average = data["temp"].mean()
# print(average)
#
# maximum = data["temp"].max()
# print(maximum)
#
# print(data.condition)
# print(data.temp)

monday = data[data.day == "Monday"]
print(monday.temp * 9/5 + 32)

# maximum = data[data.temp == data.temp.max()]
# print(maximum)

# creating a dataframe
new_data = {
    "students": ["Mike", "James", "Angela"],
    "Scores": [76, 56, 65]
}

dataframe = pandas.DataFrame(new_data)
dataframe.to_csv("students.csv")
print(dataframe)


