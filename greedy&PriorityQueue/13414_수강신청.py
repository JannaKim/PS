import sys; input= lambda: sys.stdin.readline().rstrip()

k, l= map(int, input().split())
ls=[]
for _ in range(l):
    ls.append(input())

dic={}
chk= [True]*l
for i in range(l-1,-1,-1):
    if ls[i] not in dic:
        dic[ls[i]]=True
    else:
        chk[i]=False

for i in range(l):
    if chk[i]==True:
        print(ls[i])
        k-=1
    if not k:
        break

'''
4 8
1
1
2
3
2
1
3
1
'''