def solution(n, arr1, arr2):
    answer = []

    M=0
    for a, b in zip(arr1, arr2):
        M= max(M, len(bin(a)[2:]))
        M= max(M, len(bin(b)[2:]))
    for a, b in zip(arr1, arr2):
        a= bin(a)[2:]
        b= bin(b)[2:]
        la= len(a)
        lb= len(b)
        ans=''
        if la<M:
            a='0'*(M-la)+a
        if lb<M:
            b='0'*(M-lb)+b
        for a_, b_ in zip(a, b):
            if a_=='1' or b_=='1':
                ans+='#'
            else:
                ans+=' '
        print()
        answer.append(ans)
    
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

#11111