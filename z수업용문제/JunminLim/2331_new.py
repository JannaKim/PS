n,p=map(str, input().split())
L=[]
while n not in L:
    L.append(n)
    
    a = 0
    for i in n:
        a+=int(i)**(int(p))
    n = str(a)
while n in L:
    L.remove(n)
    a = 0
    for i in n:
        a+=int(i)**(int(p))
 
    n = str(a)
print(len(L))
'''
for i in range (len(L)):
    dic[L[i], i]
    '''