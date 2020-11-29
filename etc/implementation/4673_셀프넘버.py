L=[0]*(10001)

for i in range(1,10001):
    s=i
    for el in str(i):
        s+=int(el)
    if s<=10000:
        L[s]=1

for i in range(1,10001):
    if not L[i]:
        print(i)