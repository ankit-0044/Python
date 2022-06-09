# Largest Number in the array with index value

import array

arr = array.array('i',[80,46,22,78,66,9,79,35])

largest_num = arr[0]
index_at = 0

for i in range(len(arr)):
    if (largest_num < arr[i]):
        largest_num = arr[i]
        index_at = i

print(largest_num)
print(index_at)