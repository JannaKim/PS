from sys import *
N = int(input())
L = [int(i) for i in input().split()]
found=False
idx=0

# idx 크게 만들어 놓고 break 
i=1
if L == sorted(L) or L==sorted(L)[::-1]:
    print(0)
    exit()
while i<N:
    if L[i]>=L[i-1]:
            #print(f'* L[{i}]>=L[{i-1}]')
            pass
    else:
        if found==False:
            idx=i # 개수니까
            #print('idx', idx)
            found=True
        else:
            found=False
            break
    i+=1


found2=False
idx2=0

i=1
while i<N:
    if L[i]<=L[i-1]:
            pass
            #print(f'% L[{i}]<=L[{i-1}]')
    else:
        if found2==False:
            idx2=i # 개수니까
            #print('&idx', idx)
            found2=True
        else:
            found2=False
            break
    i+=1

if found and L[-1]<=L[0] and found2 and L[-1]>=L[0]:
    print(min(idx,idx2))
elif found and L[-1]<=L[0]:
    print(idx)
elif found2 and L[-1]>=L[0]:
    print(idx2)
else:
    print(-1)


'''
5
3 4 5 1 2

5
3 5 4 1 2
'''

        
    



