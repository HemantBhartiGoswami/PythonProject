# Task 1: Create a Dictionary of Student Marks
# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

my_dic = {'john': 80, 'david': 70, 'jash': 60, 'Alice': 90}

name = str(input('Enter the student\'s name: '))
if name in my_dic:
    print(f"{name}'s marks: {my_dic[name]}")
else:
    print(f"{name} not found.")
