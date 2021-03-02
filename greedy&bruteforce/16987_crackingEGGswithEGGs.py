n= int(input())
B= []
for _ in range(n):
    a, b=map(int, input().split())
    B.append([a,b])

mx=-1



def backtrack(idx, cnt):
    global mx
    if idx==n-1:
        mx=max(mx,cnt)
        return
    thr_dur, thr_wei = B[idx]
    if thr_dur==0:
        backtrack(idx+1, cnt)
        return # 이거 안해줬었음 ㅜㅜ
    backtrack(idx+1, cnt) # 안고르고 가는것도 있어여?
    for i in range(idx+1,n):
        if not B[i][0]:
            continue
        print(f'{idx}->{i}')
        def_dur, def_wei= B[i]
        ori=def_dur
        oricnt=cnt
        #print(idx,cnt, B, '->')
        if thr_wei >= def_dur:
            cnt+=1
            B[i]=[0,0]
        else:
            def_dur-=thr_wei
            B[i]= [def_dur, def_wei]
        if thr_dur<=def_wei:
            cnt+=1
        #print(idx,cnt, B)
        backtrack(idx+1, cnt)
        cnt=oricnt
        B[i]= [ori, def_wei]

backtrack(0, 0)
print(mx)

'''
3
213 295
153 24
15 233
'''