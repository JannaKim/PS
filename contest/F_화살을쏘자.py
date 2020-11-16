N = int(input())
Q = [[] for _ in range(4)]

def gcd(a,b):
    if a==0 or b==0:
        return a+b
    if a>b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)
    
for _ in range(N):
    a, b = map(int, input().split())
    if a>=0 and b>=0:
        GCD=gcd(a,b)
        Q[0].append((a//GCD, b//GCD))
    elif a<0 and b>=0:
        a=abs(a)
        GCD=gcd(a,b)
        Q[1].append((a//GCD, b//GCD))
    elif a<0 and b<0:
        a, b =abs(a),abs(b)

        GCD=gcd(a,b)
        Q[2].append((a//GCD, b//GCD))
    else:
        b=abs(b)
        GCD=gcd(a,b)
        Q[3].append((a//GCD, b//GCD))


def find(L):
    EL = set(L)
    dic={}
    for i in EL:
        dic[i]=0

    for j in L:
        dic[j]+=1
    return max([i for i in dic.values()])

mx=0
for i in range(4):
    if Q[i]:
        mx = max(mx,find(Q[i]))

print(mx)

'''
5
8 16
10 -3
2 4
7 10
1 2


10
-14 -3
4 8
3 14
7 -14
21 -42
-3 18
-7 -7
12 24
20 -40
1 9
'''