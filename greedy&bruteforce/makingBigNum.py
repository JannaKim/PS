
def solution(number, k):
    num = list(number)
    s = [] 
    s.append(s[0]) 
    count = 0
    
    for i in range(1, len(num)):
        if count == k: 
            s += num[i:] 
            break
        s.append(num[i]) 
        if s[-1] > s[-2]: 
            while(len(s) != 1 and s[-1] > s[-2] and count < k): # 반복
                s[-2], s[-1] = s[-1], s[-2]
                s.pop() 
                count += 1 
    answer = ''.join(s) 

    return answer



