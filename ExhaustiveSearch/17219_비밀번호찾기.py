import sys; input= lambda: sys.stdin.readline().rstrip()
n, m= map(int, input().split())
dic={}
for _ in range(n):
    site, pw= input().split()
    dic[site]=pw

for _ in range(m):
    print(dic[input()])