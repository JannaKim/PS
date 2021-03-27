n, m, bloc= map(int, input().split())
fie= []
for _ in range(n): fie+=[*map(int, input().split())]

def leveling(hei):
    dig=0
    fill=0
    for acre in fie:
        if acre>hei:
            dig+=2*(acre-hei)
        else:
            fill+=hei-acre

    return (dig, fill)

ans= (1e9,0)
for i in range(257):
    dig, fill=leveling(i)
    if fill<=(bloc+(dig//2)) and dig+fill<= ans[0]:
        ans= (dig+fill, i)
print(*ans)


'''
7 7 6000
30 21 48 55 1 1 4
0 0 0 0 0 0 0
15 4 4 4 4 4 8
20 40 60 10 20 30 2
1 1 1 1 1 1 9
24 12 33 7 14 25 3
3 3 3 3 3 3 32
    
Output : 48 60
Answer : 879 10
'''