unit= [10, 2.5, 4]
#won=[1000000000000000.0, 100000000000000.0, 25000000000000.0, 10000000000000.0, 1000000000000.0, 250000000000.0, 100000000000.0, 10000000000.0, 2500000000.0, 1000000000.0, 100000000.0, 25000000.0, 10000000.0, 1000000.0, 250000.0, 100000.0, 10000.0, 2500.0, 1000.0, 100.0, 25.0, 10]
for _ in range(int(input())):
    cost= int(input())
    i=0
    ans=0
    biggest=1
    won=[]
    while biggest*unit[i]<=cost:
        biggest*=unit[i]
        won.append(biggest)
        i=(i+1)%3

    won=won[::-1]
    won.append(1)
    #print(won)
    leng=len(won)

    mn=1e15
    def zeroone(i, ans, cst):
        #print(i,ans,cst)
        if i==leng:
            global mn
            mn=min(mn, ans+cst)
            return

        if i+1<leng and won[i]/2.5==won[i+1]:
            tmp=cst
            while tmp>=won[i]:
                tmp-=won[i]
                zeroone(i+1, ans+1,tmp)
        else:
            ans+=cst//won[i]
            cst=cst%won[i]   
            zeroone(i+1, ans, cst)

    
    zeroone(0,0,cost)
    print(int(mn))