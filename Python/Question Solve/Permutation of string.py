# Python program to find number of distinct
# permutations of a string.

MAX_CHAR = 26

# function to find factorial of n.
def factorial(n) :
	
	fact = 1;
	for i in range(2, n + 1) :
		fact = fact * i;
	return fact
	
# Returns count of distinct permutations
# of str.
def countPermutation(st) :
	
	length = len(st)
	freq = [0] * MAX_CHAR
	
	# finding frequency of all the lower
	# case alphabet and storing them in
	# array of integer
	for i in range(0, length) :
		if (st[i] >= 'a') :
			freq[(ord)(st[i]) - 97] = freq[(ord)(st[i]) - 97] + 1;

	# finding factorial of number of
	# appearances and multiplying them
	# since they are repeating alphabets
	fact = 1
	for i in range(0, MAX_CHAR) :
		fact = fact * factorial(freq[i])

	# finding factorial of size of string
	# and dividing it by factorial found
	# after multiplying
	return factorial(length) // fact

# Driver code
str = "aabbcc"
st = str.lower()
print (countPermutation(st))

