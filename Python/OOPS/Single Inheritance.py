# Single Inheritance 
class Father: 			# Parent Class
	Money = 10000 			# Class Variable 

	def Show(self): 			# Instance Method
		print("Parent Class Instance Method")

	@classmethod 			# Decorator
	def ShowMoney(cls): 			# Class Method
		print("Parent Class Class Method:",cls.Money) 			# Accessing Class Variable 

	@staticmethod 			# Decorator
	def Stat (): 			# Static Method
		Value = 400
		print("Parent Class Static Method:",Value)

class Son(Father): 			# Child class
	def Disp(self): 			# Instance Method
		print("Child class Instance Method")

Son_object = Son() 			# Creating Child Class Object
Son_object.Disp() 			# Calling Child Class Instance Method
Son_object.Show() 			# Calling Parent Class Instance Method Using child Class Object
Son_object.ShowMoney() 			# Calling Parent Class Class Method Using Child Class Object
Son_object.Stat() 			# Calling Parent Class Static Mehtod using Child Class Object
print("Class Variable:",Son.Money) 			# Accessing Class Vaiable Outside The Class
