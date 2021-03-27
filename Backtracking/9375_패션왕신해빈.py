import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    dic={}
    L=[]
    kind=0
    for _ in range(int(input())):
        a, b= input().split()
        if b not in dic:
            dic[b]= 1
            #L.append(b)
            kind+=1
        else:
            dic[b]+=1
    ans=1
    for v in dic.values():
        ans*=(v+1)
    print(ans-1)
    
    '''
    
    
    def rec(i, changed,sm):
        global ans
        if changed:
            ans+=sm
        if i==kind:
            return
        rec(i+1, True,sm*L[i])
        rec(i+1,False,sm)
    rec(0,False,1)
    print(ans)
    '''