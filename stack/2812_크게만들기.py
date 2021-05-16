n, k= map(int, input().split())
num= input()
stc=[]
top=-1
for i in range(n):
    #print(digit+1, n, i)
    ths= int(num[i])
    for _ in range(top+1):
        if stc[j]<ths and n-i+j>=n-k:
            #print(stc, n,-i,j,1, n-k)
            stc[j]=ths
            for k in range(j+1,top+1):
                stc[k]=0
            break
    
    else:
        stc.append(ths)
        top+=1
print(''.join([str(el) for el in stc]))
