v = " AEIOU"
cnt = 0

def combine(* args):
    res = ''
    for idx in args:
        res += v[idx] 
    return res
        
def contribute(k):
    global cnt
    if k : cnt += 1
        
def solution(word):
    
    for i in range(1, 6):
        contribute(i)
        res = combine(i)
        
        if res == word:
            return cnt
        
        for j in range(6):
            contribute(j)
            res = combine(i, j)
            
            if res == word:
                return cnt
            if not j: continue
                
            for k in range(6):
                contribute(k)
                res = combine(i, j, k)
                
                if res == word:
                    return cnt
                if not k: continue
                    
                for l in range(6):
                    contribute(l)
                    res = combine(i, j, k, l)
                    
                    if res == word:
                        return cnt
                    if not l: continue
                        
                    for m in range(6):
                        contribute(m)
                        res = combine(i, j, k, l, m)
                        
                        if res == word:
                            return cnt
                        
                        
    return -1