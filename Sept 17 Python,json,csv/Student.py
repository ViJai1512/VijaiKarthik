# Define a simple class
class Student:
	# Constructor
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# Method
	def greet(self):
		return f'Hello, my name is {self.name} and I am {self.age} years old.'

# Create objects of the class
s1 = Student("Rahul", 21)
s2 = Student("Priya", 22)

# Call methods
print(s1.greet())
print(s2.greet())