#Creating Array
from numpy import *
print('"TAKING INPUT"')
value =int(input("Enter Number Of Elements: "))
arr = zeros( value , dtype=int)

#taking input
for num in range(len(arr)):
    print("Enter Element AT Index",num,":")
    val = int(input())
    arr[num]=val
print("\nEntered Array Elements Are:",arr)

#view method
arr2 = arr.view() #view method statement
print("View Method Array Is:",arr2)
print("\nMemory Location Of Array 1:",id(arr))
print("Memory Location Of Array 2:",id(arr2),"\n")

#Array Modification
print('"ARRAY MODIFICATION"\n')

loc = int(input("Please Enter Your Array Index To Be Modified: "))
arr[loc]= int(input("Please Enter Your Element For Array 1: "))
print("Your Array 1 After Modification:",arr,"\n")

loc = int(input("Please Enter Your Array Index To Be Modified: "))
arr2[loc] = int(input("Please Enter Your Element For Array 2: "))
print("Your Array 2 After Modification:",arr2,"\n")

print("Array 1:",arr,",","Memory Location:",id(arr))
print("Array 2:",arr2,",","Memory Location:",id(arr2),'\n')

#copy Method
print('COPY METHOD\n')
print("Array Used In Copy Method Is:",arr)
cp_arr = copy(arr) #copy method statement
print("Original Array:",arr)
print("Copy Array Is:",cp_arr,'\n')

#Array Modification
print('"ARRAY MODIFICATION"\n')

loc = int(input("Please Enter Your Array Index To Be Modified: "))
arr[loc] = int(input("Please Enter Your Array Element For Original Array: "))
print("Now Original Array Is:",arr,"\n")

loc = int(input("Please Enter Your Array Index To Be Modified: "))
cp_arr[loc] = int(input("Please Enter Your Element For Copy Array: "))
print("Now Copy Array Is:",cp_arr,'\n')

print("Original Array:",arr,',','Memory Location:',id(arr))
print("Copy Array:",cp_arr,',','Memory Location:',id(cp_arr))


