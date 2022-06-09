from numpy import *
row = int(input("Enter number of rows: "))
column = int (input("Enter number of column: "))
ndarray = zeros (( row , column ), dtype = int)
i = 0
while i < len(ndarray):
    j = 0
    while j < len(ndarray[i]):
        value = int(input("Enter element: "))
        ndarray[i][j] = value
        j += 1
    i += 1
for i in range(len(ndarray)):
    for j in range(len(ndarray[i])):
        print("At index",i,j,"value",ndarray[i][j])
        
print("\n",ndarray,"\n")

print("'Flatten Method'")
flat = ndarray.flatten()
print("\n",flat,"\n")
print("'Reshape Function'")
num_array = int(input("Enter number of array you want :"))
num_row = int(input("Enter number of row you want: "))
num_column = int(input("Enter number of column you want: "))
re = reshape(ndarray,(num_array, num_row, num_column))
print ('\n',re,'\n')
