# De La Salle University – Dasmariñas
# Luis Anton P. Imperial
# BCS22
# Tuesday, September 26, 2023

# Input: Name, Q1, Q2, Q3, Class Participation, Final Exam
# Do you want to enter new student record? Yes (1), No (2).
# Output: Grading System table.

from tabulate import tabulate

class GradingSystem_Imperial:
    def __init__(self, ref, name, grade_q1, grade_q2, grade_q3, grade_cp, grade_finalexam):
        self.ref = ref
        self.name = name
        self.grade_q1 = grade_q1
        self.grade_q2 = grade_q2
        self.grade_q3 = grade_q3
        self.grade_cp = grade_cp
        self.grade_finalexam = grade_finalexam

    def GetStudentOveralls(self, ref, name, grade_q1, grade_q2, grade_q3, grade_cp, grade_finalexam):
        grade_qt = (grade_q1 + grade_q2 + grade_q3) / 3
        grade_overall = (grade_qt * 0.4) + (grade_cp * 0.2) + (grade_finalexam * 0.4)
        if grade_overall >= 0.75:
            status = "Passed"
        else:
            status = "Failed"

        new_student = [name, grade_q1, grade_q2, grade_q3, grade_cp, grade_finalexam, grade_overall, status]

        return new_student

    def PrintDatabase(self, database):
        column_names = ["Name", "Q1", "Q2", "Q3", "CP", "Final Exam", "Grade", "Status"]
        print(tabulate(database, headers=column_names))

        # print("Name \t| Q1 \t| Q2 \t| Q3 \t| CP \t| Final Exam \t| Grade \t| Status")
        # print("---- \t| ---- \t| ---- \t| ---- \t| ---- \t| ---- \t| ---- \t| ----")
        # for entry in database:
        #     print(entry[0], "\t\t| ", entry[1], "\t| ", entry[2], "\t| ", entry[3], "\t| ", entry[4], "\t| ", entry[5], "\t| ", entry[6], "\t| ", entry[7])


loop_ref = 0
name, grade_q1, grade_q2, grade_q3, grade_cp, grade_finalexam, students = [], [], [], [], [], [], []
inputting = True
print("Welcome to the University Grading System! Please input your first student's records.")

while inputting:
    name.append(input("Name: "))
    grade_q1.append(float(input("Quiz 1 Grade: ")))
    grade_q2.append(float(input("Quiz 2 Grade: ")))
    grade_q3.append(float(input("Quiz 3 Grade: ")))
    grade_cp.append(float(input("Class Participation Grade: ")))
    grade_finalexam.append(float(input("Final Exam Grade: ")))

    students.append(GradingSystem_Imperial.GetStudentOveralls(GradingSystem_Imperial, loop_ref, name[loop_ref], grade_q1[loop_ref], grade_q2[loop_ref], grade_q3[loop_ref], grade_cp[loop_ref], grade_finalexam[loop_ref]))

    inputting_response = input("\nDo you wish to enter another student's record? (y/n): ")
    if inputting_response == "y":
        loop_ref += 1
        inputting = True
        print("\nOK. Enter your next student's details:")
    else:
        inputting = False
        print("OK. Now printing the database table.\n")
        GradingSystem_Imperial.PrintDatabase(GradingSystem_Imperial, students)