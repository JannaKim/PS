''';
for q in range(2,2+2):
    for qp in range (2,2+3):
        A[q][qp]= 1
print()
for el in A:
    for i in el:
        print(i, end='')
    print()
'''
n=int(input())
side= 4*n-3
a=[]
for i in range(side):
    a.append(['*']*side)

x= 1
while side>1:
    side-=2
    if a[x][x-1]==' ':
        color='*'
    else:
        color=' '
    for ele in range (x,x+side):
        for elel in range (x,x+side):
            a[ele][elel]=color
    x+=1

for el in a:
    for i in el:
        print(i, end='')
    print()