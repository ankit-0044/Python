# Find the trailing zero of given integer
# Input: 100
# Output: 24


n = 120
zero =0
while(n != 0):
    n = n//5
    zero += n

print(zero)