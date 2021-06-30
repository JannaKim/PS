# a= (input())
a= [ *map(int, input().split()) ]
L=[]
for t in range(0, a[0]):
    q= [ *map(int, input().split()) ]
    L += q
#print(L)
g= int(input())
for j in range(0,g):ed
    d= [ *map(int, input().split()) ]
    start = (d[0] - 1) * a[1] + ( d[1] - 1 )
    ed = (d[2] - 1) * a[1] + ( d[3] - 1 )
    print(sum( L[start : ed + 1] ))
    '''
    for v in range(int(d[0])- 1, int(d[2])- 1):
        for z in range(int(d[1])- 1, int(d[3]- 1)):
            u= u+ int(L[v][z])
            print (u)
    '';
    sum( L[a:b+1] )
    '''
