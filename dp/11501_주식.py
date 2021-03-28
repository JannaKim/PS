import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n= int(input())
    L= [*map(int, input().split())]
    if n==1:
        print(0)
        continue

    def find_max(_from):
        ans=n-1
        mx=L[n-1]
        for i in range(n-2,_from-1,-1):
            if L[i]>mx:
                mx=L[i]
                ans=i
        return ans

    sellingday=find_max(0)
    profit=0
    amount=0
    for i in range(n):
        if i==sellingday:
            profit+=amount*L[i]
            if i+1==n:break
            sellingday=find_max(i+1)
            amount=0
        else:
            amount+=1
            profit-=L[i]
    print(profit)


'''
1
11
2 6 8 7 6 5 1 2 3 4 5
'''