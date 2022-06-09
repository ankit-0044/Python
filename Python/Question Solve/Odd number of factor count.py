# find the number of elements that have odd number of factors in the given range
# Input: 22 27
# Onput: 1

def factorOddCount(n,m):
    ans = 0
    start = n
    stop = m
    
    # Factor code
    for j in range(start,stop+1):
        fact = 0
        for i in range(1,j+1):
            if (j%i == 0):
                fact += 1
        if (fact%2 == 1):
            ans += 1
    return ans
print(factorOddCount(22,27))