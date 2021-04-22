from math import *
# 난이도 true story?

n= int(input())
L=[]
for _ in range(n):
    L.append(int(input()))

def gcd(a, b):
    if a*b==0:
        return a+b
    if a>b:
        return gcd(a%b, b)
    else:
        return gcd(a, b%a)
if n>=3:
    x=gcd(abs(L[1]-L[0]), abs(L[2]-L[1]))
else:
    x=L[1]-L[0]
if n>=4:
    for a, b in zip(L[3:], L[2:]):
        x= gcd(x, abs(a-b))

ans=[]
for i in range(2,int(sqrt(x))+1):
    if not x%i:
        ans.append(i)
        ans.append(x//i)
ans.append(x)
ans=list(set(ans))
ans.sort()
print(*ans)

'''

1748 실3
15649 실3
    실3
    실3
    실3
15654 실3
    실3
    실3
    실3
15663 실3
    실2
    실2
    실2




1688 플레 5 
    플레 3
        플ㄹ 4
    골3
    골5



    골2
    골2
    골4
    골4
1197 골4
11657 골4
1865 골4
1916 골5
    골3
    골5
    실1
    골4









10868 골드1
14438 골드1
2042 골1
    11659
2015 골5
10986 골4
11660 실1
2042 골1
구간 합 구하기 플5
 알약 골5
 판다 골3
 1520 골4
 1915 골5
 15992 실1
 실1










11724 실2
1707 골4
2667 실1
4963 실2
2178 실1
7576 실1
7562 실2
16929 골4
16947 골3
16940 골4
16964 골5
    골3



1947 골3
2092 골3
2172 플레5
12950 플레5
2008 플5
1126 플2


10026 골5
14395 골5
16956 실5
5014 골5
9376 플레5
2251 실버1
16932 골4
1600 골5





2580 골4
4574 골드1
1987 골드4
14501 실4
11723 실5
1182 실2
14889 실3
14391 골3
골5
'''