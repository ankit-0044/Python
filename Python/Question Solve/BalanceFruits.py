def BalanceFruit(a,m,rs):
    if (a>m):
        return rs-(a-m)

    elif (a==m):
        return rs

    elif (a<m):
        return rs+(m-a)


a,m,rs = map(int,input().split())

ret = BalanceFruit(a,m,rs)
print(ret)