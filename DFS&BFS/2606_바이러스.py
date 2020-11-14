N = int(input())
# cp=[0]*(N+1) # dic val 두개는 못하는듯

cp = [[] for _ in range(N+1)]


links=int(input())
for _ in range(links):
    a = [int(i) for i in input().split()]
    cp[a[0]].append(a[1])
    cp[a[1]].append(a[0])





# print(cp)
chk = [0]*(N+1)
cnt=0
def f(a):
    global cnt
    if chk[a]==0:
        cnt+=1
        chk[a]=1
    else:
        return

    if cp[a]!=0:
        for lnks in cp[a]:
            f(lnks)
    
f(1)
#print(chk)
cnt-=1
print(cnt)
'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7

'''