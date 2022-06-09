# Static Method 
class School:
	num_cls = 10 			# Class Variable

	@staticmethod 			# Decorator
	def show(): 			# Static Method Without Parameter
		print("Number Of Class:",School.num_cls) 			# Accessing Class Variable Inside Static Method

	@staticmethod 
	def details(cl,sec): 			# Static Method With Parameter
		Class = cl
		Section = sec
		print("The Class in you studing:",Class,Section)

School.show() 			# Calling Static Method Without Argument 
School.details("12th","C") 			# Calling Static Method With Argument
