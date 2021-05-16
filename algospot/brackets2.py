import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    s= input()
    stc=[]
    flag=False
    for el in s:
        if el=='(':
            stc.append(')')
        elif el=='{':
            stc.append('}')
        elif el=='[':
            stc.append(']')
        else:
            ths=stc.pop()
            if ths!=el:
                flag=True
                break
    if flag:
        print('NO')
    else:
        print('YES')
