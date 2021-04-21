from math import sqrt

n=int(input())
for i in range (n):
    w,g,h,r=map(int, input().split())
    print(sqrt((h-g)**2+w**2),sqrt((g+h-2*r)**2+w**2))
