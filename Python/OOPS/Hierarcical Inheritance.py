# Hierarchical Inheritance
class Father: 			# Parent Class
	def __init__(self): 			# Parent Class Constructor
		print("Father Class Constructor")
	def showF(self): 			# Parent Class Method
		print("Father Class Method")

class Son(Father): 			# Child Class
	def __init__(self): 			# Child Class Constructor
		super().__init__() 			# Super () method used for calling parent constructor
		print("Son Class Constructor")
	def showS(self): 			# Child Class Method
		print("Son Class Method")

class Daughter(Father): 			# Second Child Class
	def __init__(self): 			# Constructor
		super().__init__() 			# Super() Method used for calling parent constructor
		print("Daughter Class Constructor")
	def showD(self): 				# Child Class Method
		print("Daughter class Method")

Son_obj = Son() 			# Son Class Object
Son_obj.showF() 			# Calling parent Class Method Using Child Class Object
print()
Daughter_obj = Daughter() 			# Daughter Class Object
Daughter_obj.showF() 			# Calling parent Class Method Using Child Class Object
