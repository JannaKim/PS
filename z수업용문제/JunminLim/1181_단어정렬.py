i=int(input())
L=[]
X=[]
for p in range(i):
    a=input()
    L.append(a)
for t in range (i):
    X.append((len(L[t]),L[t]))
X.sort()
print(X[0][1])
for a,b in zip (X,X[1:]):
    if a==b:
        continue
    if a!=b:
        
        print(b[1])
