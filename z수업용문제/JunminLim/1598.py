a, b = list(map(int, input().split()))

a-=1
b-=1
x1,y1=a//4,a%4
x2,y2=b//4,b%4

ans = abs(x1-x2)+abs(y1-y2)
print(ans)