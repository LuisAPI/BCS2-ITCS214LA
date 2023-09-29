# Creating a List
'''
    List
        - are ordered, mutable(modifiable) and contain elements of different data type(numbers, strings or objects)
            - ordered
            - mutable
            - heterogeneous
            - indexed
            - slicing        
            - common operation
                -- add
                -- remove
                -- find the length
                -- insert
'''


fruits = ["banana", "apple", "strawberry", "kiwi"]
print(fruits[2]) # strawberry
print(fruits[3]) 
# negative allows us to access list from the end
print(fruits[-1])
print(fruits[-3])

# Changing items
print(fruits)

fruits[1] = "mango"
print(fruits)

# add items - .append method allows us to add an item at the end of the list

fruits.append("dragon fruit")
print(fruits)

fruits.append("watermelon")
print(fruits)

# delete items - del() - it allows us to remove or delete items in our list

del(fruits[2])
print(fruits)

fruits.remove("watermelon")
print(fruits)


# Loop through the list
'''
    for loop is a control flow statement used for iterating over a sequence of items(list, tuple, dictionary or object)
    syntax:
        for item in iterable
            code to be executed for each item
                - for - used to initiate the loop
                - item - a variable that represents the current item in the iteration
                - in - keyword used to specify the iterable or sequence you want to loop through
                - iterable - sequence of items you want to iterate

'''
for fruit in fruits:
    print(fruit)

print("kiwi" in fruits) # True
print("apple" in fruits) # False

# length len()
print(len(fruits))

#  combine multiple list use + 

province = ["Laguna", "Cavite", "Pampanga"]
city = ["Sta Rosa", "Dasma", "San Fernando"]

country = city + province
print(country)

country.reverse()
print(country)

country.sort()
print(country)
