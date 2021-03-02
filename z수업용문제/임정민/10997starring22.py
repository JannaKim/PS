n=int(input())
# 2-(5,7) 3-(9,11) 4-(13,15) y=4x-3
side= 4*n-3
a=[]
for i in range(side+2):
    a.append(['*']*side)
if n==1:
    print('*')
    exit()
x= 1
while side>1:
    side-=2
    if a[x][x-1]==' ':
        color='*'
    else:
        color=' '
    for ele in range (x,x+side+2):
        for elel in range (x,x+side):
            a[ele][elel]=color
    x+=1

flag=False
for q in range (1,2*n-1):
    if flag==False:
        a[q][4*n-3-q]=' '
        flag=True
    else:
        a[q][4*n-3-q]='*'
        flag=False

        
    
for idx, el in enumerate(a):
    if idx==1:
        print('*')
        continue
    for i in el:
        print(i,end='')
    print()

'''
*********
*       o(1,side-1)
* *****x*
* *   o *2-2
* * *x* *3-4
* * * * *4-6
* * * * *
* *   * *
* ***** *
*       *
*********
'''
