a, b, c= map(int, input().split())
x1, x2, y1, y2= map(float, input().split())


if y2<y1:
    y1, y2= y2, y1
if x2<x1:
    x1, x2= x2, x1

if b==0 and x1<-c/a and -c/a<x2:
        print('Poor')
        exit()
elif b==0:
    print('Lucky')
    exit()
if a==0 and y1<-c/b and -c/b<y2:
        print('Poor')
        exit()
elif a==0:
    print('Lucky')
    exit()
x= float(x1)+0.1
while x<x2:
    y= (-c-a*x)/float(b)
    #print(y)
    if y1<y and y<y2:
        print('Poor')
        exit()
    x+=0.1
print('Lucky')