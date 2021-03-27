def solve():
    n = int(input())
    l = []
    for _ in range(n):
        l.append(input().split()[::-1])
    for word in input().split():
        idx = 0
        print(f'{l[idx]},{l[idx][-1]} {word}')
        while idx < n and (not l[idx] or l[idx][-1] != word):
            idx += 1
            print(f'{l[idx]},{l[idx][-1]} {word}')
        if idx == n:
            print("Impossible")
            return
        l[idx].pop()
    for i in range(n):
        if l[i]:
            print("Impossible")
            return
    print("Possible")

solve()