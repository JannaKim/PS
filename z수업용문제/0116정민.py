'''
x=int(input())

for2=[6, 2, 4 ,8]
for i in range (x):
    a,b=map(int,input().split())
    if a%10==1:
        print('1')
    elif a%10 == 0:
        print('10')
    elif a%10==2: # 2 4 8 6 2 4 8 6 
        print(for2[b%4])
    P=str(a**b)
    s= P[-1]
    print(int(s))

'''

x=int(input())
P = [0, 1, 1, 1, 2, 2] + [0]*95
#P(n)=P(n-1)+P(n-5)
for i in range (x):
    n=int(input())

    for i in range(6,n+1):
        P[i] = P[i-1] + P[i-5]

    print(P[n])



