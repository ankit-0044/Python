#passing list to function
def show (l):
    print(l)
    print(type(l))
    for i in l:
        print(i)
    return l
lst = []
n = int(input("Enter number of element: "))
i = 0
while i < n:
    lst.append(input("Enter element: "))
    i +=1
new_lst = show(lst)
print(new_lst)
print(type(new_lst))

