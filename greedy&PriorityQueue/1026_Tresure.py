n= int(input())
A= [*map(int, input().split())]
B= [*map(int, input().split())]
A.sort()
B.sort(reverse=True)

s=0
for a, b in zip(A,B):
    s+=a*b

print(s)
    