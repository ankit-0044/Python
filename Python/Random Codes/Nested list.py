#Accessing nested list using loop

a = [12,'Python',34.23,-34,['welcome','back']]
print(type(a))

n = len(a)
for i in range (n):
    if type (a[i]) is list:
        if len(a[i]) >1:
            m = len(a[i])
            for j in range (m):
                print("At index",i,j,"element:",a[i][j])
    else:
        print("At index",i,"element:",a[i])
        
