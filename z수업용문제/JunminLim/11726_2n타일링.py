n=int(input())
a=[1,2]
for i in range (n):
    a.append(a[i]+a[i+1])
print(a[-3])#%10007)