# Luis Anton P. Imperial
# BCS22
# Tuesday, 3 October 2023

# S-ITCS214LA — Data Structures & Algorithms (Laboratory)
# 231003 - Midterm Exam

# Question 3 of 27
# 35 Points
# Write an algorithm, pseudocode, and code in Python to find the maximum element in a two-dimensional array.

array = [26, 38, 11, 94, 35]

maxElement = array[0]
for element in array:
    if element > maxElement:
        maxElement = element

print("\nThe final maxElement is:", maxElement)