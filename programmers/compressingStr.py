def solution(s):
    n= len(s)
    if n<=1:
        return n
    mn=1000
    for unit in range(1, n//2+1):
        start=True
        a=''
        cnt=1
        case=''
        for i in range(0, n, unit):
            if start:
                a= s[i:i+unit]
                start=False
            elif s[i:i+unit]==a:
                cnt+=1
            else:
                if cnt!=1:
                    case+=str(cnt)
                case+=a
                a=s[i:i+unit]
                cnt=1
        
        if cnt!=1:
            case+=str(cnt)
        case+=a
        #print(case)
        mn= min(mn, len(case))
        

    return mn