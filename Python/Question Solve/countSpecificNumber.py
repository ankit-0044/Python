# Find the number of count which has 1,4,9 at their decimal places between two number
def countSpecificNum (m,n):
    count = 0
    if (m<=n):
        
        for i in range (m,n+1):
            if specificNum(i):
                count += 1
        return count
    
    return -1

def specificNum(x):
    while (x != 0):
        if (x%10 == 1 or x%10==4 or x%10==9) :
            x = x //10
        else:
            return False
    return True

m= int(input("Enter First Number:"))
n = int(input("Enter Second Number:"))
ret = countSpecificNum(m,n)
print(ret)                   