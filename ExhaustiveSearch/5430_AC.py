import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    s= input()
    n= int(input())
    L=input().split(',')
    L[0]=L[0][1:]
    L[-1]=L[-1][:-1]
    for i in range(n):
        L[i]=int(L[i])
    left=0
    right=n-1
    flipped=False
    errored=False
    for el in s:
        if el=='R':
            flipped= not flipped
        else:
            if flipped:
                right-=1
            else:
                left+=1
            if left>right+1:
                print('error')
                errored=True
                break
        if errored:
            break
    if not errored:
        if not flipped:
            if left>right:
                print('[]')
                continue
            print('[',end='')
            for i in range(left,right+1):
                print(L[i],end='')
                if i!=right:
                    print(',',end='')
            print(']')
        else:
            if left>right:
                print('[]')
                continue
            print('[',end='')
            for i in range(right,left-1,-1):
                print(L[i],end='')
                if i!=left:
                    print(',',end='')
            print(']')
