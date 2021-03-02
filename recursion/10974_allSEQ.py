n= int(input())

chk= [False]*n
def backtrack(k):
    if len(q)==n:
        print(*q)
        return
    for i in range(n):
        if not chk[i]:
            chk[i]=True
            q.append(i+1)
            backtrack(i+1)
            q.pop()
            chk[i]=False
q=[]
backtrack(0)