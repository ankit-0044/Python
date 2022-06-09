# Class Variable/ Static Variable
class Mobile:
	fp = "Yes"			#class variable

	def show(self):			# Instance Method
		print("Finger Print:",Mobile.fp) 		#Accesing class variable inside instance method
	
	@classmethod			# Decorator
	def show_model(cls):			# Class Method
		print("RealMe Finger Print:",cls.fp)  # Accessing class variable inside the class method

realme = Mobile() 			#object creation
realme.show() 		#calling instance method
Mobile.show_model()			#calling class method
print("Redmi Finger Print:",Mobile.fp)			# Accessing class variable outside the class



