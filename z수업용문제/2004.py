def gett(n, m):
    res = 0
    while n > 0:
       n = n // m
       res += n
    return res

def get(n):
    return gett(n, 2), gett(n, 5)

for  i in range(1,16):
    print(i,get(i))