import sys; input= lambda: sys.stdin.readline().rstrip()
r, c= map(int, input().split())
rg, cg, rp, cp= map(int, input().split())
room= [input() for _ in range(r)]

cnt=0
for i in range(r):
    for j in range(c):
        if room[i][j]=='P':
            cnt+=1
if cnt!=rp*cp:
    print(1)
else:
    print(0)