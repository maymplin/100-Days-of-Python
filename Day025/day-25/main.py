# with open("weather_data.csv") as file:
#     data = file.readlines()
#
#     for i in range(len(data)):
#         data[i] = data[i].strip("\n")
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)     # <_csv.reader object at 0x0000012F84AE0F40>
#
#     # for row in data:
#     #     print(row)  # ['day', 'temp', 'condition'] ['Monday', '12', 'Sunny'] and so on
#
#     temperatures = []
# to skip the first row, can do the following as well:
#   next(data)  # or
#   for row in list(data)[1:]: # or
# use csv.DictReader() to import the data in dictionary format then:
#   for row in weather:
#       temperatures.append(int(row["temp"]))
#
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


# https://pandas.pydata.org/docs/
# https://pandas.pydata.org/docs/reference/index.html
import pandas as pd

# data = pd.read_csv("weather_data.csv")
# # print(data)
# print(type(data))            # <class 'pandas.core.frame.DataFrame'>
# # print(data["temp"])
# print(type(data["temp"]))    # <class 'pandas.core.series.Series'>
#
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data["temp"].to_list()
# print(data_list)
#
# avg_temp = sum(data_list)/len(data_list)
# print(f"avg_temp: {avg_temp}")
# avg_temp_pd = data["temp"].mean()
# print(f"avg_temp_pd: {avg_temp_pd}")
# max_temp_pd = data["temp"].max()
# print(f"max_temp_pd: {max_temp_pd}")
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])   # prints out the row with max temperature

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = monday.temp
# print(type(monday_temp))
# monday_temp_in_f = int(monday.temp)*9/5 + 32
# print(type(monday_temp_in_f))

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# Central Park squirrel data
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

# Method 1
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = squirrel_data["Primary Fur Color"]
grey_squirrels_count = len(squirrel_data[colors == "Gray"])     # N.B. If size is used on a dataframe, column x row total will be returned
# print(grey_squirrels_count)
red_squirrels_count = len(squirrel_data[colors == "Cinnamon"])
# print(red_squirrels_count)
black_squirrels_count = len(squirrel_data[colors == "Black"])
# print(black_squirrels_count)

fur_color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# Method 2
fur_color_dataframe = pd.DataFrame(fur_color_dict)
fur_color_dataframe.to_csv("squirrel_count.csv")

colors2 = squirrel_data["Primary Fur Color"].value_counts()

df = pd.DataFrame(colors2)
df.to_csv("squirrel_count2.csv")

