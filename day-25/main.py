# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = (int(monday.temp) * 1.8) + 32
# print(monday_temp)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

import pandas

squirrel_data = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [],
}

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = (data[data["Primary Fur Color"] == "Gray"])
squirrel_data["Count"].append(len(gray))
cinnamon = (data[data["Primary Fur Color"] == "Cinnamon"])
squirrel_data["Count"].append(len(cinnamon))
black = (data[data["Primary Fur Color"] == "Black"])
squirrel_data["Count"].append(len(black))

new_list = pandas.DataFrame(squirrel_data)
new_list.to_csv("squirrel_count")
