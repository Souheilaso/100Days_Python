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

# import pandas
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# # print(data)
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# # import statistics
# # print(statistics.mean(temp_list))
# #
#
# # average = data["temp"].mean()
# # print(average)
# #
# # maximum = data["temp"].max()
# # print(maximum)
# #
# # print(data.condition)
# # print(data.temp)
#
# monday = data[data.day == "Monday"]
# print(monday.temp * 9/5 + 32)
#
# # maximum = data[data.temp == data.temp.max()]
# # print(maximum)
#
# # creating a dataframe
# new_data = {
#     "students": ["Mike", "James", "Angela"],
#     "Scores": [76, 56, 65]
# }
#
# dataframe = pandas.DataFrame(new_data)
# dataframe.to_csv("students.csv")
# print(dataframe)

import pandas
data = pandas.read_csv("Squirrel_Data.csv")
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(f"The number of Black Squirrels is: {black_squirrel}")
print(f"The number of Gray Squirrels is: {gray_squirrel}")
print(f"The number of Cinnamon Squirrels is: {cinnamon_squirrel}")

#dataframe
dictionary = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Squirrels Number": [black_squirrel, gray_squirrel, cinnamon_squirrel]

}
data_frame = pandas.DataFrame(dictionary)
data_frame.to_csv("new_data.csv")





















# data = pandas.read_csv("Squirrel_Data.csv")
# # Filter the DataFrame to include only black squirrels
# black_squirrels = data[data['Primary Fur Color'] == "Black"]
# gray_squirrels = data[data['Primary Fur Color'] == "Gray"]
# cinnamon_squirrels = data[data['Primary Fur Color'] == "Cinnamon"]
# # Get the count of black squirrels
# num_black_squirrels = len(black_squirrels)
# num_gray_squirrels = len(gray_squirrels)
# num_cinnamon_squirrels = len(cinnamon_squirrels)
# print("Number of Black Squirrels:", num_black_squirrels)
# print("Number of Gray Squirrels:", num_gray_squirrels)
# print("Number of Cinnamon Squirrels:", num_cinnamon_squirrels)
#
# # creating a dataframe
# data_dict = {
#     "Fur Color": ["gray", "cinnamon", "black"],
#     "Count": [num_gray_squirrels, num_cinnamon_squirrels, num_black_squirrels]
# }
# data_frame = pandas.DataFrame(data_dict)
# data_frame.to_csv("Squirrel_count.csv")
