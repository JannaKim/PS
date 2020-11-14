import sys
T = int(input())

for _ in range(T):
    a, b = [int(i) for i in input().split()]  
    cur = a+1
    end = b-1
    print(f'start = {cur}, end = {b-1}\n............')
    if b-a==1:
        print(1)
        continue
    # 주석의 cur = 현재위치, [이동]
    j = 2
    cnt = 0
    f=False # 프린트문 쓰는 용도
    while cur<end:
        if cur+j<end:
            if cur+2*j<=end:
                cnt+=2

                cur+=j
                print(f'{"cur":<6}= {cur} [{j}]')
                cur+=j
                print(f'{"cur":<6}= {cur} [{j}]')
                j+=1
            else:
                cnt+=2

                print(f'{"cur":<6}= {end} [i (2<=i<={j})], [{end-cur}-i]')
                f=True
                break
        else:
            cnt+=1
            print(f'{"cur":<6}= {end} [{end-cur}]')
            f=True
            break
    if not f:
        print(f'{"cur":<6}={end} [{end-cur}]')
    print('............')

    # ans = (nm of cur changed)+ 2
    print(cnt+2)

