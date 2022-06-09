# Using Generators inside function
lst = [1,2,3,4,5]

print(sum(lst))
print()

print(sum(num for num in lst))
print()

print(sum(range(5)))
