n= int(input())
chk=[False]*n
q=[]

def rec(Len):
    if Len==n:
        print(*q)
        return
    for i in range(n):
        if not chk[i]:
            chk[i]=True
            q.append(i+1)
            rec(Len+1)
            chk[i]=False
            q.pop()

rec(0)