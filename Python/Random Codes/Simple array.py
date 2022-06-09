from array import *
def array_fun():
    arr = array('i',[])
    value = int(input("Enter number of element: "))

    for num in range(value):
        arr.append(int(input("Enter element: ")))

    i = 0
    while i < len(arr):
        print("Index", i , "value", arr[i])
        i += 1
array_fun()
