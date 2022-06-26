#Function
def findEvenProduct(start, end):
	product = 1;
	for i in range(start, end+1):
		if(i%2 == 0):
			product *= i;
	return product;

#Driver Code
num1 = int(input());
num2 = int(input());
print(findEvenProduct(num1,num2));
