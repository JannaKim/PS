import sys; input= lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    a=input()
    b=input()
    if a==b:
        print(0)
        continue
    LenA=len(a)
    LenB= len(b)
    if LenB<LenA: # a가 짧은 길이
        a, b= b, a
        LenA, LenB= LenB, LenA
    a=list(a)
    b=list(b)

    def find(lo, hi):
        for i in range(LenB-(hi-lo)):
            #if lo==0 and hi==2:
                #print('from',i)
            flag=True
            for idx in range(hi-lo+1):
                #print(f'a[{lo+idx}]!=b[{i+idx}]:')
                if a[lo+idx]!=b[i+idx]:
                    flag=False
                    break
            if flag:
                return True
        return False


    ans=-1
    for i in range(LenA):
        for j in range(i,LenA):
            #print(i,j)
            if find(i,j):

                #print('found',j-i+1,i,j)
                ans=max(ans, j-i+1)


    if ans>0:
        print(LenA+LenB-2*ans)
    else:
        print(LenA+LenB)