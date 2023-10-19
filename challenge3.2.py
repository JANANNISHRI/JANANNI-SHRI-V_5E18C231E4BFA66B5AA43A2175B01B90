class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(students):
  students.sort(key=lambda x: x.cgpa, reverse=True)

# create a list of student objects
students = [
  Student("Alice", "001", 3.5),
  Student("Bob", "002", 3.2),
  Student("Charlie", "003", 3.8),
  Student("David", "004", 3.6)
]

# sort the list of students based on their CGPA
sort_students(students)

# print the sorted list of students
for student in students:
  print(student.name, student.roll_number, student.cgpa)