# Instannce Variable
class Mobile:
	def __init__ (self):
		self.model = "RealMe X"            # Instance Variable

	def show_model (self):
		print("Model:",self.model)		# Accessing Instance Variable

realme = Mobile()
redmi = Mobile()
python = Mobile ()
realme.show_model()
redmi.show_model()
python.show_model()
print()
redmi.model = "Redmi Note 5 Pro"
realme.show_model()
redmi.show_model()
python.show_model()

