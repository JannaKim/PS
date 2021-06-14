a,b=map(int, input().split())
Q=[]
T=[]
for i in range (a):
    f=input()
    Q.append(f)
for i in Q:
    T.append(i[::-1])
for el in T:
    print(*el,sep='')
'''
I=[]
F=[]
for i in range (a):
    F.append('0'*b)
for el in F:
    print(el)
'''

