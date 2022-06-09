# find the xor of an array
# input: 5 3 9 1 6 0 2 7
# output: 13

def xor_arr(arr):
    s = 0;
    for i in arr:
        s = s ^ i;
    return s;

arr = [5,3,9,1,6,0,2,7];
ret = xor_arr(arr);
print(ret);