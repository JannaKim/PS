n=int(input())
L=[]
for i in range (n):
    p=input()
    L.append(p)

ans=0
for i in L:
    H=[0]*26
    isGroupword=True
    for q in range (len(i)):
        if H[ord(i[q])-97]==0:
            H[ord(i)-97]=1
        else:
            if #####:
                isGroupword=False
                break
    if isGroupword==True:
        ans+=1
    