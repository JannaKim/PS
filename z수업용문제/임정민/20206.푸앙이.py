A, B, C= map(int, input().split())
#Ax+By+C
x1, x2, y1, y2= map(int, input().split())


if x2<x1:
    x1, x2= x2, x1
if y2<y1:
    y1, y2= y2, y1

if B==0:
    if A==0:
        if y1<-C and -C<y2:
            print('Poor')
            exit()
    if x1<-C/A and -C/A<x2:
        print('Poor')
        exit()
    else:
        print('Lucky')
        exit()





cur= x1+0.1
while cur<x2:
    y=(-(A*cur)-C)/B
    if y1<y and y<y2:
        print('Poor')
        exit()
    cur+=0.1



print('Lucky')