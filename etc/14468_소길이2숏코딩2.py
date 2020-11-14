ans = 0
L=[]
a=input()
for j in a:
    if j in L:
        ans+=len(L)-1-L.index(j)
        L.remove(j) 
    else:
        L.append(j)
print(ans)

'''
singun11
ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
'''
