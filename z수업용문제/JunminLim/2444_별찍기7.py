n=int(input())
m= 2*n-1
paper= [[' ']*m for _ in range(m)]
'''
paper=[]
for _ in range(m):
    paper.append([' ']*m)
'''    
p=n-1
y, x= 0, m-1
for i in range (m):
    for z in range (m):
        if abs(p-i)+abs(p-z)<n:

            paper[i][z]='*'
            
        elif (i-p)+(z-p)>=n:
            paper[i][z]=''

        elif abs(y-i)+abs(x-z)<n:
            paper[i][z]=''

        
for i in range (len(paper)):
    print(''.join(paper[i]))
