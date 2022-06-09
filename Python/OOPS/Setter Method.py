# Mutator Method / Setter Method
class Mobile:
	def __init__(self,m):
		self.model = m
	
	def set_model(self):			# Setter Method
		self.model = "Redmi Note 5 Pro"			# setting Another Value
		print("Model:",self.model)
	
realme = Mobile("RealMe x") 			# Object 
realme.set_model()			# Calling setter Method
