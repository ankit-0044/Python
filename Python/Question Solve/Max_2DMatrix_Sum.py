# Find the maximum sum of 2D matrix
# Input_1: 3
# Input_2: 3
# Input_3: [3,6,9,1,4,7,2,8,9]
# Output: 44

# importing 2D array using numpy
from numpy import *

# Defining Function
def ndarraySum(row_input, col_input, arr_2D):

	# Row Sum
	RowSum = 0
	for i in range(len(arr_2D)):
		row = 0
		for j in range(len(arr_2D[i])):
			row += arr_2D[i][j]

		if (RowSum < row):
			RowSum = row

	# Column Sum
	ColSum = 0
	for i in range(len(arr_2D)):
		col = 0
		for j in range(len(arr_2D[i])):
			col += arr_2D[j][i]

		if (ColSum < col):
			ColSum = col

	return (RowSum + ColSum)

# Driver Code
row_input = 3
col_input = 3
item_input = [3,6,9,1,4,7,2,8,9]
arr_2D = reshape(item_input,(row_input , col_input))

print(ndarraySum(row_input, col_input, arr_2D))
