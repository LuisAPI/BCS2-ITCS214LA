# Luis Anton P. Imperial
# BCS22
# Tuesday, 3 October 2023

# S-ITCS214LA — Data Structures & Algorithms (Laboratory)
# 231003 - Midterm Exam

# Question 8 of 27
# 20 Points (out of 90)
# The following code snippet is intended to remove duplicates from an array, but it is not working as expected. Write the correct snippet of code in the given spaces to fix the bug.

def remove_duplicates(arr):
    unique_arr = []
    for i in range(len(arr)):
        if arr[i] not in unique_arr:
            unique_arr.append(arr[i])
    
    return unique_arr

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)  # Schoolbook LMS doesn't support commas in this input field