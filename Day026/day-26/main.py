import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)
# print()
# for (key, value) in student_data_frame.items():
#     print(f"key = {key}")
#     print(f"value = {value}")

print()
# Loop through rows of a dataframe
for (index, row) in student_data_frame.iterrows():
    # print(f"index = {index}")
    # print(f"row = {row}")
    print(row.student)
    # print(row.score)
