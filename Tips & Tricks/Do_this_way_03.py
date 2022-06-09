# User Ternanry Operator
#Do this Way

some_condition = False

num = 6 if some_condition else 9

print(num)
print()


# Don't

some_condition = True

if some_condition:
    num = 6
else: 
    num = 9

print(num)
