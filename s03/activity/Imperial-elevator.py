# De La Salle University – Dasmariñas
# S-ITCS214LA — Data Structures and Algorithms

# Tuesday, September 19, 2023
# Luis Anton P. Imperial
# BCS22

'''
Main Activity
-   Create an elevator program in Python using Array
    -   15 floors

    start point: Ground (0)
    target point: 5

    ,-- 5   "You are in your destination"
    ,   4
    '-> 3
        2
        1
'''

import time

print(  "Welcome to The Bellevue Hotel Manila!\n"
        "15 floors of luxurious comfort at the heart of Alabang.\n"
        "(We used to be 20 floors but Godzilla chopped off 1/4th of it)\n"
    )

# 13th Floor removed due to Western cultures' triskaidekaphobia.
floorNames = ["Ground", "1st", "2nd", "3rd", "4th", "5th", "6th",
              "7th", "8th", "9th", "10th", "11th", "12th",
              "14th", "15th"]
floor = 0

def recall_floor(floorNames, floor):
    print("You are at the", floorNames[floor], "Floor.\n")

def move_elevator(floorNames, floor):
    floorTarget = int(input("Which floor do you wish to go to? 0 to 15: "))

    if floorTarget > floor:
        while floorTarget > floor:
            time.sleep(0.8)     # Change floor every 0.8 secs
            floor += 1
            print("Level: ", floor)
    else:
        while floorTarget < floor:
            time.sleep(0.8)     # Change floor every 0.8 secs
            floor -= 1
            print("Level: ", floor)
    
    return floor

isRunning = True

while isRunning == True:
    recall_floor(floorNames, floor)
    floor = move_elevator(floorNames, floor)

    print("\nDing!")
    print(  f"You are at the: {floorNames[floor]} Floor.\n"
            f"Enjoy your stay at The Bellevue Hotel Manila."
            )
    isRunning_answer = input("Stay in the elevator? (Y or N): ")
    # print(isRunning_answer)           # For debugging purposes
    if isRunning_answer.lower() == "n":
        isRunning = False
        print("*player leaves the elevator*")