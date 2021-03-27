n= int(input())
B= []
for _ in range(n):
    a, b=map(int, input().split())
    B.append([a,b])

mx=-1
def backtrack(idx, cnt):
    global mx
    mx=max(mx,cnt)
    
    if idx==n: # 마지막 계란이면 치고 종료하는거임 그냥 종료하는 게 아니라
        return
    thr_dur, thr_wei = B[idx]
    if thr_dur==0: # 지금 든 계란이 깨져있으므로 넘어간다.
        backtrack(idx+1, cnt)
        return # 이거 안해줬었음 ㅜㅜ
    for i in range(n):
        if not B[i][0] or i==idx: # 깨진계란 or 자기자신
            continue
        def_dur, def_wei= B[i]
        # ori=[def_dur, thr_dur, cnt] 이런식으로 쓰면 주소전달돼서 원본값이 유요하지 않게된다.
        cracked=0
        if thr_wei >= def_dur: # 계란깨트림
            cracked+=1
            B[i]=[0,0]
        else: # 깨지진 않았지만 내구도깎임
            B[i]= [def_dur-thr_wei, def_wei]
        if thr_dur<=def_wei:
            cracked+=1
            B[idx]= [0,0]
        else:
            B[idx]= [thr_dur-def_wei, thr_wei]
        backtrack(idx+1, cnt+cracked)
        B[i]= [def_dur, def_wei]
        B[idx]= [thr_dur, thr_wei]
    #backtrack(idx+1, cnt) # 안고르고 가는것도 있어여? 없어여
backtrack(0, 0)
print(mx)

'''
3
213 295
153 24
15 233
'''