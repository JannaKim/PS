p=[]
q=[]
r=[]
v=0
for i in range (10):
    a=int(input())
    p.append(a)
for i in range (10):
    v+=p[i]
    q.append(v)
ans=-1
for i in range (10):
    if abs(q[i-1]-100)>abs(q[i]-100):
            ans=q[i]
    if abs(q[i-1]-100)==abs(q[i]-100):
        print(q[i])
        exit()

print(ans)


