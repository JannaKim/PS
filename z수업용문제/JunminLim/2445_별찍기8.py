n=int(input())
manh=n-1
a=[]
m=2*n-1
p=2*n
paper=[[' ']*p for _ in range (m)]
'''
for i in range (len(paper)):
    print(''.join(paper[i]))
'''

y1, x1 = n-1, 0
y2, x2= n-1, 2*n
for i in range (m):
    for z in range (p):
        if abs(x1-z)+abs(y1-i)<n:
            paper[i][z]='*'
        elif abs(x2-z)+abs(y2-i)<n+1:
            paper[i][z]='*'
for i in range (len(paper)):
    print(''.join(paper[i]))


