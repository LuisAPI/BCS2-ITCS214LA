# De La Salle University – Dasmariñas
# S-ITCS214 – Data Structures and Algorithms

# Tuesday, November 7, 2023
# Session 6: Stack

# Luis Anton P. Imperial

# push operation adds the element to the top of the stack
# Create an empty
stack = []

# pushing or adding elements to the stack
stack.append(5)
stack.append(10)

print("Stack Elements")
print(stack)

class PushStack:
    def __init__(self, max_size):
        # Create an empty
        self.stack = []
        # initialize top as -1 to represent an empty stack
        self.top = -1
        self.max_size = max_size
    
    def is_full(self):
        return self.top == self.max_size - 1
    
    def is_empty(self):
        return self.top == -1
    
    def push(self, data):
        if not self.is_full():
            if data not in self.stack:
                self.top += 1
                self.stack.append(data)
                # check if the stack is successfully pushed
                return True
            else:
                # element is already in stack
                return False
        else:
            # Stack is full or overflow
            return "Stack Overflow"
    
    def display_elements(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Elements in the stack:")
            for i in range(self.top + 1):
                print(self.stack[i])


# Creating a stack with a maximum size of 5
stack = PushStack(5)

# Pushing elements onto the stack
print(stack.push("Jin"))
# Displaying elements in the stack
stack.display_elements()

print(stack.push("Jungkook"))
# Displaying elements in the stack
stack.display_elements()

print(stack.push("V"))
# Displaying elements in the stack
stack.display_elements()

print(stack.push("Jimin"))
# Displaying elements in the stack
stack.display_elements()

print(stack.push("Suga"))
# Displaying elements in the stack
stack.display_elements()

print(stack.push("Jhope"))
# Displaying elements in the stack
stack.display_elements()


# Mini-Activity
'''
    Improved the codebased to display the "Stack Overflow", "Empty" and "Element is already stack"
'''