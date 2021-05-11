from bisect import bisect_left as br
def solution(info, query):
    dic={}
    for el in info:
        a, b, c, d, e=el.split()
        A=['-',a]
        B=['-',b]
        C=['-',c]
        D=['-',d]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        if A[i]+B[j]+C[k]+D[l] not in dic:
                            dic[A[i]+B[j]+C[k]+D[l]]=[]
                        dic[A[i]+B[j]+C[k]+D[l]].append(int(e))
    for k in dic.keys():
        dic[k].sort()
    answer = [0]*len(query)
    for idx,el in enumerate(query):
        el=el.replace('and','')
        ths=el.split()
        num=int(ths[-1])
        el=''.join(ths[:-1])
        el=el.replace(' ','')
        if el in dic:
            ln=len(dic[el])
            tmp=br(dic[el],num)
            if tmp==-1:
                answer[idx]+=ln
            else:
                
                answer[idx]+=(ln-br(dic[el],num))

    
    return answer

