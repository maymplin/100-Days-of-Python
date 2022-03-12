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

data = pd.read_csv("weather_data.csv")
# print(data)
print(data["temp"])
