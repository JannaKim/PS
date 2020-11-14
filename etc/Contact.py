# (100+1+ | 01)+

import sys
T = int(input())

for _ in range(T):
    wv = input()
    start=0
    end=len(wv)
    div=2
    for idx in range(start, end+div, div):
        if start+div>len(wv)-1: # and start!=end+div: # 인덱스 초과 방지
            print('NO1', start, end+div) #? 포문이 돌았으면 안됐음
            #print('NO')
            break

        if wv[start:start+div] == '01': # 01
            pass
        elif wv[start:start+div+1] == '100': # 100+1+
            while wv[start+div] == '0':
                if start+div+1>len(wv)-1: # 끝까지 갔으면
                    print('YES')
                    start=end+div
                    break
                div+=1
            while wv[start+div] == '1':
                if start+div+1>len(wv)-1: # 끝까지 갔으면
                    print('YES')
                    start=end+div
                    break
                div+=1
        else:
            '''
            if start!=end+div:
                print('NO', start, end+div)
                break
            '''
            print('NO2', start, end+div)
            break
        if start!=end+div:
            start=start+div
            div=2


'''
3
10010111
011000100110001
0110001011001
'''
