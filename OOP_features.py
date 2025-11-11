# features in OOP
# 1. Abstraction -Hiding unnessary details from the user through classes and objects.
# 2. Encapsulation - Restrict direct access to some attributes and methods
# 3. Inheritance - mechanism to create a new class using details of an existing class without modifying it.
# 4. Polymorphism - ability to use a common interface for multiple forms (data types).



# 1. Abstraction -Hiding unnessary details from the user through classes and objects.

print("\n\n")
print("------Abstraction Example: -------\n")

class Student:
    #method to initialize the object
    def __init__(self, name, age, grade): # constructor method with initialization
        self.name = name  # properties of the class
        self.age = age
        self.grade = grade

    def student_details(self):  # method(function) of abstraction because it can't be seen in output
        print(f"{self.name} is {self.age} years old and in grade {self.grade}.")

    def student_average_age(self, age1, age2): # method(function) of abstraction because it can't be seen in output
        average_age = (age1 + age2) / 2
        print(f"The average age of the students is {average_age}.")

student1 = Student('Smit',23, 'A') # creating an object of the Student class
student2 = Student('Yunika',21, 'B')

student1.student_details()
student2.student_details()
student1.student_average_age(student1.age, student2.age)

print("\n")
print("------Encapsulation Example: -------")

# 2. Encapsulation - Restrict direct access to some attributes and methods of
#  an object and can prevent the accidental modification of data.
# Eg: I make SSN private so that it can't be accessed or modified directly outside the class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private attribute

    def display_info(self):
        if self.__age >= 18:
            print(f"{self.name} is {self.__age} years old.")
        else:
            print(f"{self.name}'s age is hidden.")


person1 = Person("Alice", 20)
person2 = Person("Bob", 16)  # Hiding the internal state of the object and requiring all interaction to be performed through an object's methods.

person1.display_info()
person2.display_info()

print("\n\n")

print("------Inheritance Example: -------\n\n")

#3. Inheritance - mechanism to create a new class using details of an existing class without modifying it.

class GradStudent(Student):  # Inheriting from the Student class
    def __init__(self, name, age, grade, major):
        super().__init__(name, age, grade)  # calling the constructor of the parent class
        self.major = major
    
    def grad_student_details(self):
        print(f"{self.name} is a graduate student majoring in {self.major}.")

    def student_details(self):
        return super().student_details()  # using method from the parent class

Student3 = GradStudent('John', 25, 'A', 'Computer Science')
Student3.student_details()  # using method from the parent class
Student3.grad_student_details()

print("\n\n")

print("------Polymorphism Example: -------\n\n")

# 4. Polymorphism - same method name but different functionality.

#polymorphism example
class CreditCard:
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."

class PayPal:
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."

class Bitcoin:
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin."
    



# Polymorphism in action
for payment in [CreditCard(), PayPal(), Bitcoin()]:
    print(payment.pay(100))    

class Teacher:
    def show_role(self):
        return "I teach students."

class Student:
    def show_role(self):
        return "I study lessons."

class Principal:
    def show_role(self):
        return "I manage the school."

people = [Teacher(), Student(), Principal()]
print("\n\n")

for person in people:
    print(person.show_role())

print("\n\n")
