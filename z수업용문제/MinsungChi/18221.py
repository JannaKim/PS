a= int( input())
L=[]
y1= 0
y2= 0
x1=0
x2=0
for j in range(0, a):
    L.append(list(map(int, input().split(' '))))
for i in range(0, a):
    for  k in range(0, a):
        if L[i][k]==5:
            y1= i
            x1= k
        if L[i][k]==2:
            y2=i
            x2=k
#print(y1, x1, y2, x2)
if (y1-y2)**2+ (x1- x2)**2<25:
    print(0)
    
else: 
    y, x = min(y1,y2), min(x1, x2)
    sero, garo = abs(y1-y2), abs(x1-x2)

    t = 0
    #print(y, x, sero, garo)
    for q in range(y,y + sero+1):
        for g in range(x, x + garo+1):
            if L[q][g]==1:
                t=t+1
                
    
    if t>=3:
        print(1)
    else:
        print(0) 

    

'''
7
0 2 0 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 0 0
0 0 0 1 1 0 0
0 0 0 0 0 5 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
'''


