# find the last third consonant from the string
# input: asdfguihj
# output: g

def third_consonant(str):
    c = 0
    ans = ''
    for i in range(len(str)-1,-1,-1):
        if (c < 3 and (not str[i]=='a') and (not str[i]=='e') and (not str[i]=='i') and (not str[i]=='o') and (not str[i]=='u')):
            ans = str[i]
            c += 1

    return ans

str = 'asdfguihj'
ret = third_consonant(str)
print(ret,end='')