a=int(input())
b=int(input())
c=int(input())
P=list(str(a*b*c))
L=[0]*10

for i in range (len(P)):
    
    L[ int(P[i]) ] +=1





for q in range (10):
    print(L[q])