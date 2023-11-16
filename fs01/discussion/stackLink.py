# Stack linked list

'''
Class Node:
    def __init__ (self, x):
        self.data = x
        self.next = None
    
Class Stack:
    def __init__(self):
        self.top = None


Operations:
    Push    - insertion at the beginning
    Pop - deletion from the beginning

Insertion
    - Case 1
        - stack is Empty (Top is None)
            new = Node(10)
            self.Top = new
            Top.next = None
    - Case 2
        - stack is Empty
            new = Node(20)
            new.next = top
            top = new
            new = Node(30)
            top = top.data
    - Case 3
        - stack with more than one element
            temp = top
            top = temp.next
            temp = None
Display
    - Case 1
        - stack empty
            if top is None
                print("Empty")
    - Case 2
        temp = top
        while temp
            print(temp.data)
            temp = temp.next
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self):
        x = int(input("Enter element to be inserted into Stack: "))
        new = Node(x)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print("Popped Element is: ", self.top.data)
            print("-----------------------------------")
            self.top = None
        else:
            temp = self.top
            print("Popped Element is: ", self.top.data)
            print("-----------------------------------")
            self.top = temp.next
            temp = None
    
    def display(self):
        if self.top is None:
            print("Stack is Empty")
            print("-----------------------------------")
        else:
            print("Elements of the stack are: ")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print("Top of the Stack is: ", self.top.data)

s = Stack()
while(True):
    print("Enter the option below")
    print("1 - Push Operation\n 2 - Pop Operation \n 3 - Display \n 4 - Exit")
    option = int(input())
    if option == 1:
        print("PUSH OPERATION")
        print("--------------")
        s.push()
    elif option == 2:
        print("POP OPERATION")
        print("--------------")
        s.pop()
    elif option == 3:
        print("DISPLAY")
        print("--------------")
        s.display()
    else:
        break