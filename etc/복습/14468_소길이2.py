S = input()
L = []
[L.append([]) for i in range(ord('Z')-ord('A')+1)]

for i in range(len(S)):
    L[ord(S[i])-65].append(i)
print(L)

cnt=0
for i in range(ord('Z')-ord('A')+1):
    dic={}
    for j in range(L[i][0]+1, L[i][1]):
        if S[j] not in dic:
            dic[S[j]]=True
        else:
            dic[S[j]]=False
    cnt+=sum([1 for value in dic.values() if value == True])

print(cnt//2)
'''
ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
'''
    
