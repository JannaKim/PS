N = int(input())
a, b = 0, 1 #end= 0, 1
for i in range(1,N):
    a,b = a+b,a
print(a+b)