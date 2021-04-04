import sys; input= lambda: sys.stdin.readline().rstrip()
m= int(input())
Set= set()
for _ in range(m):
    inp= input()
    if inp[0]=='a':
        if inp[1]=='d':
            ths=int(inp.split()[1])
            if ths not in Set:
                Set.add(ths)
        else:
            Set=set(range(1,21))
    elif inp[0]=='r':
        ths= int(inp.split()[1])
        if ths in Set:
            Set.remove(ths)
    elif inp[0]=='c':
        ths=int(inp.split()[1])
        if ths in Set:
            print(1)
        else:
            print(0)
    elif inp[0]=='t':
        ths=int(inp.split()[1])
        if ths in Set:
            Set.remove(ths)
        else:
            Set.add(ths)
    else:
        Set.clear()