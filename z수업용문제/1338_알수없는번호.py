import sys; input= lambda:sys.stdin.readline().rstrip(); r=range
a, b= map(int, input().split())
if a>b: a,b=b,a
x, y= map(int, input().split())
a=((a-y)-1)//x+1
b=(b-y)//x+1

print(a,b)
if b-a==1:
    print(a*x+y)
else:
    print('Unknwon Number')