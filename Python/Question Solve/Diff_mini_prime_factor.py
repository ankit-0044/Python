# Return the difference of integer n with its minimum prime factor
# input: 350
# output: 358

def prime_diff(n):
    temp = n;
    i = 2;
    while(n != 1):
        if (n%i == 0):
            return (temp -i);
        else:
            i += 1;
ret = prime_diff(int(input()));
print(ret);