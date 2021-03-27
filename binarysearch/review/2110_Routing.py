n, c= map(int, input().split())

L= [int(input()) for _ in range(n)]
L.sort()

def install(k):
    global n,c
    stock=c-1
    cur=L[0]
    for el in L[1:]: 
        if el-cur>=k: #k보다 같거나 먼저기일때만 설치함
            stock-=1
            cur=el #마지막 설치 장소 바꿈

    if stock>0:
        return False
    return True

def BS():
    lo=1
    hi=int(1e9)
    ans=0
    while lo<=hi:
        m= (lo+hi)//2
        if install(m): # 설치할수있으면 늘려보기
            ans=m
            lo=m+1
        else:
            hi=m-1
    return ans

print(BS())

'''
1 2 4 8 9
'''