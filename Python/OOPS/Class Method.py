# Class Method 
class Student:
	sa = "Yes"			# Class Variable
	@classmethod			# Decorator
	def show (cls):			# Class Method Without Parameter
		print("Student available:",cls.sa)			# Accessing Class Variable Inside Class Method
	@classmethod
	def details(cls, n, r):			# Class Method With Parameter
		cls.name = n
		cls.roll = r
		print("Name:",cls.name, "Roll:",cls.roll)

Student.show()				# Calling Class Method Without Argument
Student.details("Python", "3.8")				# Calling Class Method With Argument
print("Class Variable:",Student.sa)			# Accessing Class Variable Outside the Class
print("Name:",Student.name)
print("Roll:",Student.roll)
