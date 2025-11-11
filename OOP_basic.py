class Student:
    #method to initialize the object
    def __init__(self, name, age, grade): # constructor method with initialization
        self.name = name  # properties of the class
        self.age = age
        self.grade = grade

    def student_details(self):
        print(f"{self.name} is {self.age} years old and in grade {self.grade}.")

    def student_average_age(self, age1, age2):
        average_age = (age1 + age2) / 2
        print(f"The average age of the students is {average_age}.")

student1 = Student('Smit',23, 'A') # creating an object of the Student class
student2 = Student('Yunika',21, 'B')

student1.student_details()
student2.student_details()

student1.student_average_age(student1.age, student2.age)

#modifying a property
student1.age = 24
print(student1.__dict__)  # Displaying the properties of student1 after modifying age

#deleting a property
del student1.age
print(student1.__dict__)  # Displaying the properties of student1 after deleting age

#delete the object
del student2
# print(student2.__dict__)  # This will raise an error since student2 is deleted