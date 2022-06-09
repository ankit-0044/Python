# Instance Method 
class Mobile:
	def __init__(self,m):			# Constructor with Parameter
		self.model = m			# Instance Variable

	def show_model(self):			# Instance Method Without Parameter
		print("Model:",self.model)			# Accessing Instance Variable Inside Instance Method
	
	def show_price(self, p):			# Instance Method With Parameter
		price = p
		print("Price:",price)

realme = Mobile("RealMe x")			# Object Creation and Passing Actual Argument To Construtor parameter 
realme.show_model() 			# Calling Instance Method without Argument
realme.show_price("Rs.10000")			# Calling Instance Method With Argument
print()
redmi = Mobile("Redmi Note 5 Pro")
redmi.show_model()
redmi.show_price("Rs.10500")
