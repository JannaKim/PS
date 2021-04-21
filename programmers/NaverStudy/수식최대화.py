from itertools import permutations as permu
def solution(expression):
    op= ['+', '-', '*']
    ans=0
    for cse in permu([0,1,2], 3):
        cse=list(cse)
        A=expression.split(op[cse[0]])
        As=[]
        #print(A)
        for b in A:
            C=''
            B=[]
            for c in b.split(op[cse[1]]):
                C=eval(c)
                #print('C',C)
                B.append('('+str(C)+')')
            #print('B',B)
            if len(B)>1:
                B=op[cse[1]].join(B)
                As.append('('+str(eval(B))+')')
            else:
                As.append('('+str(B[0])+')')
        #print(As)
        if len(As)>1:
            ans=max(ans,abs(eval(op[cse[0]].join(As))))
        else:
            ans=max(ans,int(eval(As[0])))
    #print(ans)

    return ans

print(solution(	"50*6-3*2"))