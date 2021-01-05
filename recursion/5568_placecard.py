# 5568 카드놓기.py
n= int(input())
k= int(input())

L=[input() for _ in range(n)]

ans= []
def selection(floor, sel, bit, s):
    if sel==k:  
        ans.append(s)
        return
    for i in range(n):
        if bit[i]=='0':
            tmp= bit[:]
            tmp[i]='1'
            selection(floor+1, sel+1, tmp,s+L[i])

    if floor== n+1: # 초과
        return


selection(0,0,list('0'*n), '')
ans=set(ans)
ans=list(ans)
print(len(ans))