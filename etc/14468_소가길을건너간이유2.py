S = input()
dic={}
for i in range(65,91):
    dic[chr(i)]=True

for i in range(65,91):
    if chr(i)*2 in S:
        dic[chr(i)]=False

    S=S.replace(chr(i)*2,'')
#print(S)
chk={}
#[chk[key]=False for key,value in dic.items() if value==True] 이거 안돼

for key,value in dic.items():
    if value==True:
        chk[key]=False
L=[]
for a in range(len(S)):
    L.append((S[a],a))
L.sort(key= lambda x:x[0])
#print(L)

_from=0
_to=0
pair=set()
for i in range(0,len(S),2):
    _from=L[i][1]
    _to=L[i+1][1]
    temp={}
    for j in range(_from+1,_to):
        if S[j] not in temp:
            temp[S[j]]=True
        else:
            temp[S[j]]=False
    for key,value in temp.items():
        if value==True:
            pair.add(L[i][0]+key if ord(L[i][0])<ord(key) else key+L[i][0])
    
#print(pair)
print(len(pair))
    





'''
ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
'''