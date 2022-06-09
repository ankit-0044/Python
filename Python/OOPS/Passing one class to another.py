# Passing Member Of The One Class To Another Class

class Student:
	def __init__(self,n,r): 			# Constructor With Parameter
		self.name = n 			# Instance Variable
		self.roll = r

	def disp(self): 			# Instance Method
		print("Student Name:",self.name) 			
		print("Student Roll:",self.roll)

class User:
	@staticmethod 			# Decorator
	def show(detail): 			# Static Method With Parameter
		print("User Name:",detail.name) 			# Accessing Instance Variable Inside Static Method
		print("User Roll:",detail.roll)
		print()
		detail.disp() 			# Calling Instance Method Inside Static Method

st = Student("Python", 3.7) 			# Object Creation and Passing Actual Argument to the Constructor
User.show(st) 			# Calling Static Method And Passing Object as a Argument 
