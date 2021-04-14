def solution(s):
    mx= len(s)
    ans = mx
    for i in range(mx//2,0,-1): # 자르는 단위
        prv=''
        accum=1
        tmp=mx
        for j in range(0,mx,i):
            ths=s[j:j+i]
            if prv==ths:
                tmp-=i
                accum+=1
            else:
                if accum>1:
                    tmp+=len(str(accum))
                    accum=1
            prv=ths
        if accum>1:
            tmp+=len(str(accum))
        ans= min(ans, tmp)
        #print(i,tmp)
    
    return ans
'''
num=99
cnt=1
while num>=10:
    num//=10
    cnt+=1
print(cnt)
'''