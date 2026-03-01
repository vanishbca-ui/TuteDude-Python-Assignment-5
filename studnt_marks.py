
student_marks = {
    "Amit": 85,
    "Rahul": 90,
    "Priya": 78,
    "Neha": 92,
    "Vikas": 88
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(name + "'s marks are:", student_marks[name])
else:
    print("Student not found in the dictionary.")