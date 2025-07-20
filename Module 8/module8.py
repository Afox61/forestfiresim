import json

def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load student data
with open("student.json", "r") as file:
    students = json.load(file)

print("Original Student List:")
print_students(students)

# Add new student
new_student = {
    "F_Name": "Abigail",
    "L_Name": "Fox",
    "Student_ID": 99999,
    "Email": "abigailfox@gmail.com"
}

# Only add if not already in the list
if new_student not in students:
    students.append(new_student)

print("\nUpdated Student List:")
print_students(students)

# Save updated data
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nStudent JSON file has been updated.")

