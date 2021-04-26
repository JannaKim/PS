p=[]
l=[0]*31
ans=[]
for i in range (28):
    n=int(input())
    p.append(n)
p.sort()
for i in p:
    l[i]=1
for i in range (1,31):
    if l[i]==0:
        ans.append(i)

for i in range (len(ans)):
    print(ans[i])