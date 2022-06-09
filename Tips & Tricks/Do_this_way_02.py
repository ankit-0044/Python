# Remove Duplicate items from list
# Do this way
my_list = [1,3,4,6,7,8,3,2,1,9,7,4,3,19]

new_list = list(set(my_list))

print(new_list,"\n")

# Don't 

my_list = [1,3,4,6,7,8,3,2,1,9,7,4,3,19]

new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

