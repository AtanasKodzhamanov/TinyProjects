
#To do
#Write this to a csv
#Add GUI
#Use pandas for charts
#Add goals section
#Add daily emails showing past 7 days compared to previous 7 days.

import pandas as pd
import datetime
from datetime import date
from datetime import datetime #?


data_path='D:\Programming\GitHub Connected Repo\TinyProjects\HabitTracker\\Habits.xlsx'
habits_df = pd.read_excel (data_path)
lastdate=pd.to_datetime(habits_df["Date"][:-1])
today=date.today()
diff=today-lastdate
# add rows 

def create_new_habit():
    new_habit=input("Add new habit's name: ").lower()
    habits_df[new_habit]=""
    print(f"{new_habit} added to your list.")
    habits_df.to_excel(data_path)

def update_habit():
    update_habit = (input("Which habit do you want to update: ")).lower()
    value = int(input("Add value. 1/0 for binary habits, or a number for time: "))
    column=list(habits_df[update_habit])
    column.append(value)
    habits_df[update_habit]=pd.Series(column)
    print(habits_df[update_habit])
    habits_df.to_excel(data_path)

update_habit()
# def delete_habit():
#     pass

# def analytics():
#     pass

# #print using a dictionary/list
# print("Command list:")
# print("Exit")
# print("Create habit")
# print("List habits")
# print("Update habit")
# print("")

# #make a dictionary for the commands
# while True:
#     command=input("Input command: ")
#     print("")
#     if command=="Exit":
#         break
#     elif command=="Create habit":
#         create_new_habit()
#     elif command=="List habits":
#         print(dict_habits)
#     elif command=="Update habit":
#         update_habit()

# with open('test4.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile)
#     writer.writeheader()
#     writer.writerows(dict_habits)