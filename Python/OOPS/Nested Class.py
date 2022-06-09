# Nested Class
class Army (object): 			# Outer Class
	def __init__(self): 			# Outer Class Constructor
		self.name = "Python" 			# Outer Class Instance Variable
		self.Inner_object = self.Gun() 			# Creating Object(Inner_object) Of Inner Class (Gun)

	def show(self): 			# Instance Method
		print("Name:",self.name) # Accessing Instance Variavle Of Outer Class

	class Gun: 			# Inner Class
		def __init__(self): 			# Inner Class constructor
			self.name = "AK47" 			# Inner Class Instance Variable
			self.capacity = "75 Rounds" 
			self.length = "34.3 Inch" 
		def disp(self): 			# Inner class Instance Method
			print("Gun Name:",self.name) 			# Accessing Instance Variable of Inner class
			print("Gun Capacity:",self.capacity)
			print("Gun Length:",self.length)

Outer_object = Army() 			# Creating Object For Outer Class
Outer_object.show() 			# Calling Instance Method Of Outer Class
print()
print("Gun Name:",Outer_object.Inner_object.name) 			# Accessing Inner Class Instance Variable Using Object Of Outer Class To Outside The Class
Outer_object.Inner_object.disp() 			# Calling Inner Class Instance Method 
print()
assign = Outer_object.Inner_object 			# Assigning Outerclass and Innerclass Object Value To Another Variable
assign.disp() 			# Calling Inner Class Instance Method Using Newly Assigned Variable
print()
Inner_object2 = Army().Gun() 			# Creating New Object Of Inner class
Inner_object2.disp() 			# Calling Instance Method Of Inner Class Using New object
