# Luis Anton P. Imperial
# BCS22
# Tuesday, 3 October 2023

# S-ITCS214LA — Midterm Exam
# Question 26 of 27
# 10 Points (out of 90)
# The following code snippet is intended to reverse an array, but it is not working as expected. Identify and fix the bug. And choose the expected output.

def reverse_array(arr):
    for i in range(len(arr) // 2):
        temp = arr[i]
        arr[i] = arr[len(arr) - i - 1]
        arr[len(arr) - i - 1] = temp
    
numbers = [1, 2, 3, 4, 5]
reverse_array(numbers)
print(numbers)

# Select the correct response(s):
# ✅ There is no bug in the code