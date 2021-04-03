N= int(input())
n=N
cnt=0
while True:
    cnt+=1
    n=(n%10)*10+(n//10+n%10)%10
    if n==N:
        print(cnt)
        break