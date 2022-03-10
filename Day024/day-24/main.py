# Video 220
# Python documention - https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# file = open("my_file.txt")
#
# contents = file.read()
#
# print(contents)
#
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # writes over existing file with "w" mode
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nHello there.")

# if a file doesn't yet exist when trying to write to a file, Python will create the file automatically
with open("new_file.txt", mode="w") as file:
    file.write("A brand new file.")
