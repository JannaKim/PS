def solution(encrypted_text, key, rotation):
    ans= encrypted_text
    rotation = rotation % len(key)
    ans = ans[rotation:] + ans[:rotation]

    
    print(ans)
    answer=''
    for a, b in zip(ans,key):
        mv = ord(b)-96
        if ord(a)-mv >=97:
            #print(f'{a}->{chr(ord(a)-mv)}')
            answer = answer + chr(ord(a)-mv)
        else: #넘어서면
            answer = answer + chr(ord(a)-mv+26)
    

    

    
    return answer

print(solution('qyyigoptvfb', 'abcdefghijk', 3))
#print(solution('hellopython', 'abcdefghijk', 3))