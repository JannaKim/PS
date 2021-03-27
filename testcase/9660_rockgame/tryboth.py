
import sys; input= lambda: sys.stdin.readline().rstrip(); e=enumerate
n=0
for i in range(1000000,10000000):
    n=i
    ans=-1
    #n= int(input())
    if not n%7 or n%7==2:
        ans=2
    else:
        ans=1

    n= str(n)[::-1]

    rule= (1,3,2,6,4,5)

    one=0
    for idx, num in e(n):
        one+=int(num)*rule[idx%6]

    ls= [*map(int, list(n))]

    c=0
    if int(ls[0])>=5:
        c=1
    ls[0]=(ls[0]+5)%10
    if c:
        for idx, num in e(ls[1:]):
            tmp=(ls[idx+1]+c)%10
            if ls[idx+1]>tmp:
                ls[idx+1]=tmp
            else:
                ls[idx+1]=tmp
                break
    two=0
    for idx, num in e(ls):
        two+=num*rule[idx%6]

    if not one%7 or not two%7:
        if ans!=2:
            print(ls)
            print(n,ans)
            exit()
    else:
        if ans!=1:
            print(ls)
            print(n,ans,one,two)
            exit()