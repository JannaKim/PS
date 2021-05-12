def solution(dartResult):
    dartResult= dartResult.replace('*','! ')
    dartResult= dartResult.replace('#','@ ')
    dartResult= dartResult.replace('S','**1 ')
    dartResult= dartResult.replace('D','**2 ')
    dartResult= dartResult.replace('T','**3 ')
    dartResult=dartResult.split()
    n= len(dartResult)
    for i in range(n):
        if dartResult[i]=='!':
            dartResult[i]=''
            dartResult[i-1]*=2
            if 0<=i-2:
                if dartResult[i-2]:
                    dartResult[i-2]*=2
                else:
                    if 0<=i-3:
                        dartResult[i-3]*=2

        elif dartResult[i]=='@':
            dartResult[i]=''
            dartResult[i-1]*=-1
        else:
            dartResult[i]=eval(dartResult[i])
        
    ans=0
    for el in dartResult:
        if el:
            ans+=int(el)

    return ans

print(solution("1D#2S*3S"))
