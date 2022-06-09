# Find 2 dice possible sum

# Method 1

num = int(input("Enter Number: "))
possible_count = 0

if (num < 2 or num > 12):
    possible_count = 0

else:
    for x in range(1, 7):
        if (num - x <= 6 and num - x > 0):
            possible_count += 1

print(possible_count)
print()

# Method 2

num = int(input("Enter Number: "))
possible_count = 0

if (num > 12 or num < 2):
    possible_count = 0

else:
    for i in range(1, 7):
        for j in range(1, 7):
            if (i + j == num):
                print(f"Possible Faces are:{i},{j}")
                possible_count += 1
print(f"Possibility are: {possible_count}")
