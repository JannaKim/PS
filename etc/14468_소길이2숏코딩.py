def solve(string) :
    idx = [ord(c)-0x41 for c in string]
    print(idx)
    v = [0 for i in range(26)]
    cnt = 0
    for i in range(len(idx)) :
        v[idx[i]] ^= 1 # 1 0 바꾸기
        if v[idx[i]] == 0 :
            j = i-1
            while idx[j] != idx[i] :
                cnt += v[idx[j]]
                j -= 1
    return cnt

print(solve(input()))

'''
ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
'''