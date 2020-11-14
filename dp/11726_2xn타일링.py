n=int(input())
p=[]
p.append(1)
p.append(2)
for i in range(2,n):
    p.append((p[i-1]+p[i-2])%10007)

print(p[n-1])
  
#1793

