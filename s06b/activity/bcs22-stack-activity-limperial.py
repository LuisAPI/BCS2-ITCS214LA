# De La Salle University – Dasmariñas
# S-ITCS214LA — Data Structures & Algorithms (Laboratory)
# 11.11

# Luis Anton P. Imperial
# BCS22

"""
Create a task manager in python using stack with basic functionalities:
 (classes, methods, lists, loops, input-handling in python )
 - add tasks with a title and descriptiom
 - mark tasks as completed
 - display the list of tasks along with status
 - exit option to exit the task manager
 push in your gitHub account and paste the URL in our SB- lab
 bcs21-stack-activity-ffernandez.py
"""

import time

version = 1.0

class TaskManager:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size
        self.top = -1

    def isFull(self):
        if self.top == self.max_size - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push_task(self, new_task):
        if new_task.content not in self.stack:
            if not self.isFull():
                self.stack.append(new_task)
                self.top += 1
                return f"New task added! {new_task.content}"
            else:
                return  f"No more tasks can be added! Max number of tasks is: {self.max_size}. Delete some."
        else:
            return f"Your task, “{new_task.content}”, is already in the notebook!"
        
    def mark_finished(self, taskNumInput):
        number = int(taskNumInput)

        # Use when 'isFinished' variable suspected of not being read properly
        # print(f"Currently, task #{number}'s completion is:", self.stack[number - 1].isFinished)

        self.stack[number - 1].isFinished = True
        
        print(f"Task #{number} marked as completed.")

    def pop_task(self, taskNumInput):
        number = int(taskNumInput)
        
        self.stack.pop(number - 1)

        print(f"Task #{number} successfully deleted.")
    
    def display_tasks(self):
        if not self.isEmpty():
            for taskNum in range(len(self.stack)):
                print(f"Task #{taskNum + 1}")
                print(self.stack[taskNum])
        else:
            print("There are no tasks on your notebook.")

    def print_menu(self):
        print(f"Rushgoal Task Manager v{version}.")
        print("")

        print("Enter the number of your choice to interact with the program.")
        print("1 — Create new task.")
        print("2 — Mark a task as completed.")
        print("3 — Delete a task.")
        print("4 — Show all tasks.")
        print("5 — Exit the program.")
        print("")

        print("© 2023 Luis Anton P. Imperial.")
        print("Check the GitHub repository for your non-exclusive license.")
        print("")

        menu_option = int(input("Your option: "))
        print("")

        return menu_option

class Task:
    def __init__(self, content, description):
        self.content = content
        self.description = description
        self.isFinished = False

    def __str__(self):
        taskFormat = f"""
Task: {self.content}.
Description: {self.description}.
Completed? {self.isFinished}
"""

        return taskFormat

def main():
    running = True

    notebook = TaskManager(5)
    while running:
        selected_option = notebook.print_menu()
        if selected_option == 1:
            print("Create a new task —")
            print("")

            new_task_content = input("Content: ")
            new_task_desc = input("Description: ")
            createdTask = Task(new_task_content, new_task_desc)
            print("")

            notebook.push_task(createdTask)
        elif selected_option == 2:
            task_to_complete = input("Which task do you wish to mark as finished? ")

            notebook.mark_finished(task_to_complete)
        elif selected_option == 3:
            deletion_message = "Which task do you wish to delete?\nInput the task's number count.\nTask #: "

            task_to_delete = input(deletion_message)

            notebook.pop_task(task_to_delete)
        elif selected_option == 4:
            notebook.display_tasks()
        elif selected_option == 5:
            print("Byerrrrsss!")
            break
        elif selected_option == 6:
            # Debugging option

            print("The first item in the stack is:")
            print(notebook.stack[0])
        else:
            print("Invalid option! Try again.")
            print("")
        print("----")
        print("Loading main menu...")
        print("")
        time.sleep(2)


main()
