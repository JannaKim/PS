t=int(input())
z=0
for i in range (t):
    h,w,n=map(int, input().split())
    p=((n-1)//h)
    q=n-(p*h)
    print((p+1)+100*(q))      