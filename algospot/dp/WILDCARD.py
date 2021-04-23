def tst(chk,i,j,card,m,n):
    #print(chk,i,j,card,m,n)
    if i>=m:
        return True
    if j>=n:
        return False
    ret=False
    if card[j]!='*':
        if chk[i]==card[j] or card[j]=='?':
            ret= ret or tst(chk,i+1,j+1,card,m,n)
        else:
            return False
    else:
        while card[j]=='*':
            j+=1
            if j==n:
                return True
        
        for k in range(i,m):
            if chk[k]==card[j] or chk[k]=='?':
                ret= ret or tst(chk,k+1,j+1,card,m,n)
    return ret


for _ in range(int(input())):
    s= input()
    n= len(s)
    ans=[]
    m= int(input())
    for _ in range(m):
        ths=input()
        if tst(ths,0,0,s,len(ths),len(s)):
            ans.append(ths)
    [print(el) for el in sorted(ans)]


'''
a*b
3
abbab
acb
ab
'''