n, m, e= map(int, input().split())
edge= [[] for _ in range(n)]
ans =1e9
L=[int(i) for i in input().split()]
for i in range(len(L)):
    edge[i]=L[i]
for i in range(n-m-1):
    hi= i+m-1
    a= edge[hi]-edge[i]
    if edge[i]>e:
        a+=edge[i]-e
    elif edge[hi]<e:
        a+=e-edge[hi]
    ans= min(ans,a)
print(ans)

'''
6 3 7
2 4 5 8 11 12

4
'''