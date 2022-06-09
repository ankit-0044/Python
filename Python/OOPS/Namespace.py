# Namespace 
class Mobile:
	fp = "Yes"			# Class variable

	@classmethod			# decorator
	def show_model(cls):			# Class Method
		print("Finger Print:",cls.fp) # Accessing Class Variable Inside the Class method
# Object Creation
realme = Mobile()
redmi = Mobile ()
realme.show_model()			# Accessing Class Method 
redmi.show_model()
print()
print("Class:",Mobile.fp)			# Accessing Class Variable Outside the Class 
print("RealMe:",realme.fp)
print("Redmi:",redmi.fp)
print()
Mobile.fp = "No"			# Modifying Class variable For Whole Class
print("class:",Mobile.fp)
print("RealMe:",realme.fp)
print("Redmi:",redmi.fp)
print()
realme.fp = "Not Working"			# Modifying class Variable Only For realme object
print("class:",Mobile.fp)
print("RealMe:",realme.fp)
print("Redmi:",redmi.fp)
