# De La Salle University – Dasmariñas
# S-ITCS214LA — Data Structures & Algorithms (Laboratory)

# Thursday, November 16, 2023
# Main Activity — Palindra-palooza
# Determine if an input statement is a case-insensitive palindrome.

# Luis Anton P. Imperial
# BCS-2-2

class Node:
    def __init__(self, node_input):
        self.data = node_input
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self, push_input):
            new_element = Node(push_input)

            if self.top is None:
                self.top = new_element
                self.top.next = None
            else:
                new_element.next = self.top
                self.top = new_element
    
    def pop(self):
        if self.top is None:
            print("There is no sentence input to pop!")
        else:
            popped_element = self.top.data
            self.top = self.top.next
            return popped_element

    def display(self):
        if self.top is None:
            print("No sentence to test!")
            print("")
        else:
            print("Your sentence, squished into one word, is: ")
            temp = self.top
            all_elements = []
            while temp:
                all_elements += temp.data
                temp = temp.next
            
            print("".join(all_elements))


class PalindromeChecker:
    def __init__(self, stack_object_input):
        self.stack_object_used = stack_object_input.lower()

    def customization_options(self):
        characters_allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        return characters_allowed

    def isPalindrome(self):
        sentence = []
        reversed_sentence = []
        characters_to_check_for = self.customization_options()

        for character in self.stack_object_used:
            if character in characters_to_check_for:
                sentence.append(character)
                stack_object.push(character)

        ### For debugging purposes — Letters pushed and popped:
        # print(letters_pushed, letters_popped)
        # print("")

        stack_object.display()

        for character in self.stack_object_used:
            if character in characters_to_check_for:
                popped_element = stack_object.pop()
                reversed_sentence.append(popped_element)

        ### For debugging purposes — Sentences to test:
        print("Your sentence is: ", sentence)
        print("Your reversed sentence is: ", reversed_sentence)
        print("")

        return sentence == reversed_sentence
    
    @staticmethod
    def display_menu():
        print("Welcome to RennmontTech Palindrome Checker!")
        print("")

        print("A palindrome is a sentence that, when backwards, is read the same way, ignoring spaces, punctuation and capitalization.")
        print("")

        menu_input = input("Enter your sentence: ")

        return menu_input

        
def main():
    while True:
        user_input = PalindromeChecker.display_menu()
        print("")
        
        sentence_to_check = PalindromeChecker(user_input)

        if sentence_to_check.isPalindrome() is True:
            print("The sentence is a palindrome because it reads the same forward and backward, ignoring spaces, punctuation, and capitalization.")
        else:
            print("The sentence is not a palindrome. A palindrome is a sentence that, when backwards, is read the same way, ignoring spaces, punctuation and capitalization.")
        print("")

        running_input = input("Do you wish to check again? (y/n): ")
        if running_input.lower() in ['n', "no", "false", "f"]:
            break

if __name__ == "__main__":
    stack_object = Stack()
    main()