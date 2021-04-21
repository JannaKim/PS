a,b=map(int, input().split())
x=[]
y=[]
for i in range (a):
    p=list(input())
    x.append(p)
for i in range (a):    
    q=input()
    y.append(q)
r=[]
for i in range (a):
    for j in range (2*b):
        
        if y[i][j]!= x[i][j//2]:
            print('Not Eyfa')
            exit()
print('Eyfa')

#P=''.join(r)
#print(P)
#print(x)
#print(y)
#print(r)
'''
if x==y:
    print('Eyfa')
else:
    print('Not Eyfa')
y랑 r을 비교
'''