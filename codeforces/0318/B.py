import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    s= input()
    zeroOver=False
    flag=True
    for a, b in zip(s,s[1:]):
        if not zeroOver:
            if a=='1' and b=='1':
                zeroOver=True
                continue
        else:
            if a=='0' and b=='0':
                flag=False
                break
    if flag:
        print('YES')
    else:
        print('NO')