import sys; input= lambda: sys.stdin.readline().rstrip()
L=[]
mx=-1
for _ in range(5):
    tmp=list(input())
    mx=max(mx,len(tmp))
    L.append(tmp+['']*15)


for i in range(mx):
    for j in range(5):
        print(L[j][i],end='')
