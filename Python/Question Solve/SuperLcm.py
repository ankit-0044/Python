# SuperLCM : Find the LCM and power of two integer and multiply the sum of LCM to Power
# Input: 6
# Output: 612

# Full Code
def SuperLCM(n):
    ans = 0
    # LCM Code
    for j in range(1,n+1):
        lar = max(j,n)
        small = min(j,n)
        i = lar
        while(1):
            if(i%small == 0):
                break
            i += lar
        # multiply LCM and power
        ans += i * pow(j,n-j)
    return ans

print(SuperLCM(50))