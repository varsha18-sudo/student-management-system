students = []

def add_student(name, roll_number):
student = {
"name": name,
"roll_number": roll_number
}
students.append(student)
return student

def get_students():
return students

if **name** == "**main**":
add_student("Rahul", 101)
print("Student Management System")
print(get_students())
