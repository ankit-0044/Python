# Multi-level Inheritance 
class Father:           # Parent Class
    def __init__(self):
        print("Father Class Constructor.")
    def showF(self):
        print("Father Class Instance Method.")

class Son(Father):          # Child Class
    def __init__(self):
        super().__init__()
        print("Son Class Constructor.")
    def showS(self):
        print("Son Class Instance Method.")

class Grandson(Son):            # GrandChild Class
    def __init__(self):
        super().__init__()
        print("Grandson Class Constructor.")
    def showG(self):
        print("Grandson Class Instance Method.")

Grandson_obj = Grandson()           # Grandchild Class Object
Grandson_obj.showF()            # Calling Method
Grandson_obj.showS()
Grandson_obj.showG()
