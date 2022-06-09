# find the maxmimum integer from the string
# input: 33 milestone is either 12 or 75 miles away
# output: 75

def max_int(str):
    str_split = str.split();
    ans = -1;
    for i in str_split:
        if (i.isdigit()):
            i = int(i);
            if ans < i:
                ans = i;
    return ans;

str = '33 milestone is eithr 12 or 75 miles away';
ret = max_int(str);
print(ret,end='');