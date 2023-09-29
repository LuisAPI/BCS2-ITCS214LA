# De La Salle University - Dasmariñas
# Luis Anton P. Imperial
# BCS22
# Tuesday, September 12, 2023

# 1.) Write a Python program that will compile for the bonus using the specifications stated.
# T&M Group of Companies gives longevity bonus to their employee based on their number of years of service and their
# salary using the following conditions.

# 5 years == 5%; 10y == 100%; 15y == 150%; 20y == 200%

# 2.) Compute for the running of the program.

def compute_bonus(name, years_served, salary):
    bonus = 0
    running_time = 1

    if 10 > years_served >= 5:
        running_time += 1
        bonus = salary * .05
    elif 15 > years_served >= 10:
        running_time += 2
        bonus = salary * 1
    elif 20 > years_served >= 15:
        running_time += 3
        bonus = salary * 1.5
    elif years_served >= 20:
        running_time += 4
        bonus = salary * 2

    total_comp = salary + bonus

    print(f'Hi, {name}! You have served {years_served} years at T&M, earning a regular salary of ₱{salary}.\n'
          f'Your bonus is: ₱{bonus}.\n'
          f'Your total compensation is: ₱{total_comp}.')


if __name__ == '__main__':
    name_input = input("Enter your name: ")
    years_served_input = int(input("How many years have you served?: "))
    salary_input = float(input("Enter your salary: "))

    print('')
    compute_bonus(name_input, years_served_input, salary_input)
