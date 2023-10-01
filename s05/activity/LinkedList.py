'''
    linked-list
        - is basically a data structure for storing collection of data or items.

    class Box {
        int data
        Box next
    }

    head.data
        - the data - head represents the first box

    box next
        - reflects to the next box that is connected to a particular box
'''

import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):     # Added in V2
        return self.data    # Added in V2

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def rearrange(self):
        current = self.head
        to_replace = [3, 4]   # Defaults are '3' and '4'

        # print("The values of 'temp' are: ", temp[0], " and ", temp[1])

        print("\nRearranging the list...")
        time.sleep(1)

        while current:
            if current.__repr__() == to_replace[0]:
                print(to_replace[1], end=" -> ")
                current = current.next

            elif current.__repr__() == to_replace[1]:
                print(to_replace[0], end = " -> ")
                current = current.next

            else:
                print(current.data, end=" -> ")
                current = current.next
        print("None")

        time.sleep(1)
        print("\nArray values swapped!")

# Input values
input_values = [6, 3, 4, 2, 1]

my_linked_list = LinkedList()
for value in input_values:
    my_linked_list.insert(value)

# Display the linked list
my_linked_list.display()

my_linked_list.rearrange()


