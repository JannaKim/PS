from collections import deque
n= int(input())
L= [*map(int, input().split())]
def fac(n):
    if n==0: return 0
    s=1
    for i in range(1,n+1):
        s*=i
    return s


if L[0]==1:
    def cal(num, q, leng):
        q.sort()
        if len(q)==1:
            return str(q[0])
        a=q.pop(0)
        amount= fac(leng-1)
        while num>amount:
            q.append(a)
            a= q.pop(0)
            num-=amount
        return str(a)+' '+cal(num, q, leng-1)

    q= list(range(1,n+1))
    print(cal(L[1], q, n))

else:
    def cal(q):
        if len(q)==1:
            return 1
        a=q[0]
        L= sorted(q)
        return L.index(a)*fac(len(q)-1)+ cal(q[1:])

    q= L[1:]
    print(cal(q))


'''
3 2 4 1
'''