import sys; input= lambda: sys.stdin.readline().rstrip()
#?
for _ in range(int(input())):
    n= int(input())
    L=[*map(int, input().split())]
    dic={}
    for i in L:
        if i not in dic:
            dic[i]=0
        dic[i]+=1

    A=sorted([k for k in dic.values()])
    
    print(A)
    while len(A)>2:
        print(A)
        
        ths= min(A)
        A=[el-ths for el in A]
        A.sort()

        print(A)
        start=0
        for idx,el in enumerate(A):
            if el!=0:
                start=idx
                break
        A=A[start:][:]
    if len(A)==2:
        if A[0]==A[1]:
            print(0)
        else:
            print(abs(A[0]-A[1]))
    else:
        print(A[0])

