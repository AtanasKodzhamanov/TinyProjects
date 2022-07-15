
#To do
#Write this to a csv
#Add GUI
#Use pandas for charts
#Add goals section
#Add daily emails showing past 7 days compared to previous 7 days.

import pandas as pd

habits = pd.read_excel ('G:\\My Drive\\05. Programming\\Habit tracker\\Habits.xlsx')

def create_new_habit():
    new_habit=input("Add new habit's name: ").lower()
    print(f"{new_habit} added to the dictionary.")

def update_habit():
    update_habit = (input("Which habit do you want to update: ")).lower()
    value = int(input("Add value. 1/0 for binary habits, or a number for time: "))
    dict_habits[update_habit].append(value)
    print(dict_habits[update_habit])

def delete_habit():
    pass

def analytics():
    pass

#print using a dictionary/list
print("Command list:")
print("Exit")
print("Create habit")
print("List habits")
print("Update habit")
print("")

#make a dictionary for the commands
while True:
    command=input("Input command: ")
    print("")
    if command=="Exit":
        break
    elif command=="Create habit":
        create_new_habit()
    elif command=="List habits":
        print(dict_habits)
    elif command=="Update habit":
        update_habit()

with open('test4.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile)
    writer.writeheader()
    writer.writerows(dict_habits)