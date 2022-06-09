# Constructor with Super() Method 
class Father:           # Parent Class
    def __init__(self,m):           # Parent Class Constructor
        self.money = m          # Instance Variable
        print("Father Class Constructor.")
    def show(self):             # Instance Method
        print("Father Class Instance Method.")

class Son(Father):          # child Class
    def __init__(self,m,j):             # Child Class Constructor With Parameter
        super().__init__(m)             # Super() Method For Calling Parent Class Constructor or Prevent Constructor Overriding
        self.job = j
        print("Son Class Constructor.")
    def disp(self):
        print("Salary:",self.money)             # Accessing Instance Variable Of Parent class
        print("Job:",self.job)          # Accessing Instance Variable Of Child class 

Son_object = Son("Rs.25000","Programmer")           # Creating Object And Providing Actual Argument to the Child Calss Constructor
Son_object.disp()           # Calling Child Class Instance Method
