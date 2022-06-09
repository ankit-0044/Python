# Accessor Method / Getter Method
class Mobile:
	def __init__(self,m):
		self.model = m
	
	def get_model(self):			# Getter Method
		return self.model			# Returning Instance Variable Value 

redmi = Mobile("Redmi Note 5 Pro")			# Object and Passing Actual Argument
m = redmi.get_model()			# Calling Getter Method and Receiving Returning Value to Another variable
print("Model:",m)			# Printing Returning Value