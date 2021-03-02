n= int(input())
dp= [[0]*4 for _ in range(max(n,3)+1)]
'''
dp[i][0]: i째가 위가 1*2짜리로 삐져나옴
dp[i][1]: i째가 아래가 1*2짜리로 삐져나옴
dp[i][2]: i째가 다 참, 끝에 1*2짜리가 아님
dp[i][3]: i쨰가 1*2 두개로 채워져있음
'''
a= [0]*4
b= [0]*4
c= [0]*4

a[0]= 0
a[1]= 0
a[2]= 2
a[3]= 0

b[0]= 1
b[1]= 1
b[2]= a[2]*2+ a[0]*2+ a[1]*2
b[3]=1

prvprvsum= sum(a)
if n==1:
    print(sum(a))
    exit()
if n==2:
    print(sum(b))
    exit()
tmp= a[:]
print(prvprvsum)
print(b)
print(c)
for i in range(3, n+1):
    c, prvprvsum= [(b[2]//2+ b[1])%(int(1e9)+7), (b[2]//2+ b[0])%(int(1e9)+7), sum(b)*2%(int(1e9)+7), prvprvsum%(int(1e9)+7)], sum(b)%(int(1e9)+7)
    b=c[:]
    print(prvprvsum)
    print(b)
    print(c)
print(sum(c)%(int(1e9)+7))

