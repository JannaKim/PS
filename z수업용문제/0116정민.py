x=int(input())
for i in range (x):
    a,b=map(int,input().split())
    if a%10==1:
        print('1')
    elif a%10 == 0:
        print('10')
    elif a%10==2:
        if b%4 == 0:
            print('6')
        elif b%4 == 1:
            print('2')
    P=str(a**b)
    s= P[-1]
    print(int(s))