from sys import *
N = int(input())
SEQ=[int(input()) for _ in range(N)] # 받은 수열
ans=[]


Q=[]
num=0 # 1에서 N으로 순차적으로 바뀜

while SEQ:
    if not Q: # 스택이 비었을땐
        ans.append('+')
        num+=1
        Q.append(num) # 안넣은 다음 숫자 Q에 push

    # len(Q)=1일때 Q[-1]이 안된다.. 
    last_q=Q.pop() #먼저 맨 뒤에꺼를 꺼내보고, pop할 상황이 아니면 다시 넣는 식

    if SEQ[0]>last_q:
        
        Q.append(last_q) # 기존의 last_q 다시 스택에 넣는다

        num+=1
        #print('+')
        ans.append('+')
        Q.append(num) # 안넣은 다음 숫자 Q에 push
        #print(Q)
    elif SEQ[0]==last_q:
        ans.append('-')
        if not SEQ:
            break
        del SEQ[0] # 맨앞 SEQ 지운다
        #print(Q)
        

    else: # seq<last_q: 불가능한 경우
        print('NO')
        exit()


[print(i) for i in ans]

    

'''
8
4
3
6
8
7
5
2
1

5
1
2
5
3
4
'''



