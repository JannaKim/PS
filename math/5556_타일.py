n = int(input())
n -= 1
for _ in range(int(input())):
    a , b = map(int, input().split())
    a -= 1
    b -= 1
    a = min(a , n-a)
    b = min(b , n-b)
    print(min(a , b)%3 + 1)
