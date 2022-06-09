# Multiple Inheritance
class Father: 			# parent Class 
	def __init__(self): 			# Constructor
		super().__init__() 
		print("Father Class Constructor")
	def showF(self):
		print("Father Class Method")

class Mother: 			# Parent Class
	def __init__(self): 			# Constructor
		super().__init__()
		print("Mother Class Constructor")
	def showM(self):
		print("Mother Class Method")

class Son(Father,Mother): 			# Child Class With Multiple parent
	def __init__(self): 			# Constructor
		super().__init__()
		print("Son Class Constructor")
	def showS(self):
		print("Son Class Method")

Son_obj = Son () 			# Son Class Object
Son_obj.showF() 			# Calling Parent Class Method
Son_obj.showM() 			# Calling Parent Class Method
