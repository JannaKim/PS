#시간 초과
N = int(input())
L = [int(i) for i in input().split()]

seq=[[1, L[0], L[0], [L[0]]]] # [len, first, last, array]
firsts=[L[0]]
lasts=[L[0]]
#print(seq)
for i in range(1,N):
    #print(f"L[{i}]={L[i]}검사중")
    appendable=0
    for j in range(len(seq)):
        #print(f"seq[{j}] 검사중")
        test = sorted(lasts+[L[i]])
        if test[0]!=L[i]: # 그럼 L[i]는 기존 배열들 중에 바로 붙일 수 있는 경우 존재.
            appendable=1
        if seq[j][1]<L[i] and L[i]<seq[j][2] and appendable==0: # first 와 last 사이에 L[i]이 있으면 L[i]을 마지막으로한 배열 생성
            A=sorted(seq[j][3]+[L[i]])
            A=A[:(A.index(L[i])+1)]
            seq.append([len(A),seq[j][1],L[i],A]) 
            lasts.append(L[i])
            #print(f"first 와 last 사이에 {L[i]} 있다, {seq}")
        elif L[i]>seq[j][2]: # last보다 크면 append
            seq[j][0]+=1
            if seq[j][2] in lasts: # 기존 lasts 에 있는 last지우고
                lasts.remove(seq[j][2])
            seq[j][2]=L[i]
            seq[j][3]=seq[j][3]+[L[i]]
            lasts.append(L[i]) # lasts 에 새 last 담는다.
            #print(f"{L[i]}가 last보다 크므로, {seq}")
    
    if min(firsts)>L[i]: # 이 경우 L[i]이 first인 배열 새로 생성
        seq.append([1,L[i],L[i],[L[i]]])
        firsts.append(L[i])
        #print(f"{L[i]}이 first인 배열 새로 생성, {seq}")
maxi=0
for l in range(len(seq)):
    length=seq[l][0]
    if length>maxi:
        maxi=length

print(maxi)
