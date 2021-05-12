def solution(n, t, m, timetable):
    table=[]
    for el in timetable:
        a= [int(i) for i in el.split(':')]
        table.append(a[0]*60+a[1])
    table.sort(reverse=True)
    cur= 9*60-t
    box= [[0,[]] for _ in range(n)]
    for time in range(n):
        cur+=t
        for _ in range(m):
            if not table:
                break
            ths=table.pop()
            if ths<=cur:
                box[time][0]+=1
                box[time][1].append(ths)
                
            else:
                table.append(ths)
                break
    print(box)
    for i in range(n-1,-1,-1):
        tmp= 9*60+t*i
        if box[i][0]<m:
            a=tmp//60
            b=tmp%60
        else:
            if len(set(box[i][1]))==1:
                if tmp<box[i][1][0]:
                    time=box[i][1][0]-1
                    a=time//60
                    b=time%60
                    return f'{a:0>2}:{b:0>2}'
            else:
                time=sorted(box[i][1])[-1]-1
                a=time//60
                b=time%60
                return f'{a:0>2}:{b:0>2}'
                    
            
            return f'{a:0>2}:{b:0>2}'
    print(box)
                
        
    
    answer = ''
    return answer

print(solution(2,10,2,["09:10", "09:09", "08:00"]))


