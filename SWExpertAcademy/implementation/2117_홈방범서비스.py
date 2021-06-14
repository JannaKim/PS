t = int(input())
def manhattan(y , x , i , j):
    return abs(y-i) + abs(x - j)
for tst in range(1,t+1):
    n , m = map(int, input().split())
    mp = [ [*map(int, input().split())] for _ in range(n)]
    ans = 0
    for K in range(2*n):
        opcost = (K ** 2) + ((K - 1) ** 2)
        domain = K - 1
        for y in range(n):
            for x in range(n): # mid = y , x
                house = 0
                for i in range(n):
                    for j in range(n):
                        if mp[i][j] and manhattan(y , x , i , j) <= domain:
                            house +=1
                profit = (house * m) - opcost
                if 0 <= profit:
                    ans = max(ans , house)

    print(f"#{tst} {ans}")



'''
1
8 3
0 0 0 0 0 1 0 0
0 1 0 1 0 0 0 1
0 0 0 0 0 0 0 0
0 0 0 1 0 1 0 0
0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 0 1 0
1 0 0 0 0 0 0 0
'''