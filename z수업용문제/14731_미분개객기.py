#WA

M=int(1e9)+7
s=0
dic={}
def f(r):
    if r==0:
        return 1
    if r in dic:
        return dic[r]
    half= f(r//2)
    dic[r//2]=half
    if r%2:
        return half*half*2%M
    else:
        return half*half%M
        
for _ in range(int(input())):
    a, b= [*map(int, input().split())]
    s+=(a*b*f(b-1))%M
print(s)
