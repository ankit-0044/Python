class Mobile ():
    def __init__(self,m,p):
        self.model = m
        self.price = p
    def show_Details(self):
        print(f"Model: {self.model}")
        print("Price: {}".format(self.price))

def details ():
    Model = input("Enter model name: ")
    Price = int(input("Enter price: "))
    return Model , Price

print("Details of RealMe Mobile")
m , p = details()
realme = Mobile(m,p)
realme.show_Details()
print(id(realme))
print()

print("Details of Redmi Mobile")
m, p = details()
redmi = Mobile(m , p )
redmi.show_Details()
print(id(redmi))
