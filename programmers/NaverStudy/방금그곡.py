'''
멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다
그 곡이 네오가 들은 곡이 아닐 수도 있다
 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다

  음악 제목, 재생이 시작되고 끝난 시각, 악보를 

   여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다

    음악은 반드시 처음부터 재생되

라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한
 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다
'''
def solution(m, musicinfos):
    lm=len(m)
    mxLen=0
    answer="(None)"
    for el in musicinfos:
        st, ed, name, note =el.split(',')
        st= int(st[:2])*60+int(st[3:])
        ed= int(ed[:2])*60+int(ed[3:])
        dur= ed-st
        played=[]
        n= len(note)
        idx=0
        t=dur
        while t:
            ths=note[idx%n]
            played.append(ths)
            if ths!='#':
                t-=1
            idx+=1
            if t==0 and note[idx%n]=='#':
                played.append("#")
                break
        played=''.join(played)
        #print(played)

        ln= len(played)
        for i in range(ln-lm+1): # prob!
            #print(name,played[i:i+lm])
            if played[i:i+lm]==m:
                
                if i+lm< ln and played[i+lm]=='#':
                    continue
                #print(played[i:i+lm],'=',m, dur, mxLen)
                if dur>mxLen:
                    mxLen=dur
                    answer=name

    return answer

#print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

print(solution("C#C",["03:00,03:02,FOO,C#CB", "04:00,04:06,BAR,C#C#"]))