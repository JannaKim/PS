x=list(input())
y=1
previous = -1
a =10
b= 26
for i in range (len(x)):
    if previous == x[i]:
        a=9
        b=25    
    else:
        a=10
        b=26
    if x[i]=='c':
        y=y*b
    if x[i]=='d':
        y=y*a
    previous= x[i]
print(y)