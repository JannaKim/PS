n,m=map(int, input().split())
P= {}
for i in range (m):
    a,b=map(int, input().split())
    # P.append((a,b))
    if a>b:
        a, b = b, a
    P[(a, b)] = 0 # P[key] = value

    
Q=[]
for i in range (1,n+1):
    for j in range (i+1,n+1):
        for k in range (j+1,n+1):
            Q.append((i,j,k))

#n ** 3

ans = 0
for I in Q: # n**3 
    IA = (I[0], I[1])
    IB = (I[0], I[2])
    IC = (I[1], I[2])

    if IA not in P: 
        if IB not in P:
            if IC not in P: # 1
                ans += 1

print(ans)
    # I = [a, b, c]
        # Ia = (I[0] + I[1]]
        # Ib = 
        # Ic




'''
if Ia in P: # m
    Q.remove(Ia)

  

m * n^3


m * n^3 + n **3

print(Q)
'''