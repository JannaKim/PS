import sys; input= lambda: sys.stdin.readline().rstrip()

def solution(words):

    words.sort()
    ans = 0

    prv_end=0
    for a, b in zip(words, words[1:]):
        if a[0]!=b[0]:
            ans+=max(1, prv_end)
        else:
            len_a= len(a)
            len_b= len(b)
            if len_a<len_b:
                a+=' '*(len_b-len_a)
            elif len_b<len_a:
                b+=' '*(len_a-len_b)
            print(a, b, 'start')
            for idx, (x, y) in enumerate(zip(a, b)):
                #print(x, y)
                if x==y:
                    #print('same')
                    continue
                    
                else:
                    #print('diff')
                    if x==' ' or y==' ':
                        ans+=max(idx,prv_end)
                        print('ans',max(idx,prv_end))

                    else:
                        print('.',idx,prv_end+1)
                        if idx<=prv_end+1:
                            ans+=prv_end+1
                        else:
                            ans+=idx

                        print(ans)
                    
                    prv_end=idx
                    #print('prv_end=',prv_end)
                    print(prv_end)
                    break
    print('ans',ans)

    print(prv_end)
    if words[-1][0]!=words[-2][0]:
        ans-=1
    else:
        ans+=prv_end

    return ans

print(solution(["go","gone","guild"]))
#print(solution(["abc","def","ghi","jklm"]))
#print(solution(["word","war","warrior","world"]	))
