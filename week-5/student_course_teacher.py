from datetime import datetime

class User:
  def __init__(self, name):
    self.name = name

class Student(User):

  students = []

  def __init__(self, name, grade, age):
    User.__init__(self, name)  
    assert type(age) == int, "Age must be Integer!"
    self.grade = grade 
    self.age = age
    self.courses = []

    student = {"name": name, "age": age}
    Student.students.append(student)

  def display(self):
    print(f"Name: {self.name}")  
    print(f"Grade: {self.grade}")
    print(f"Age: {self.age}")
    print("Courses:")
    for course in self.courses:
      print(course, course.teacher)
      

  def add_course(self, course):
    self.courses.append(course)
  @classmethod  
  def get_students(cls):
      return cls.students

class Course:

  def __init__(self, name, code, teacher):  
    assert type(name) == str, "Name must be a string"  
    self.name = name
    self.code = code
    self.teacher = teacher

  def __repr__(self):
    return f"Course: {self.name} ({self.code})"

class Teacher(User):

  def __init__(self, name):
    self.name = name
  def __str__(self):  
    return f"Teacher({self.name})"


teacher1 = Teacher("John")

programming = Course("Python", 1001, teacher1)  
math = Course("Algebra", 1002, teacher1)

student1 = Student("Sarah", 4, 21)
student2 = Student("David", 3.9, 20) 

student1.add_course(programming)
student2.add_course(math)


student2.display()
student1.courses.append(math)
student1.display()
print(Student.get_students())
