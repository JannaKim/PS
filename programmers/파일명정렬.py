def solution(files):
    m=len(files)
    new=files[:]
    file=[[] for _ in range(m)]
    dic={}
    for idx,f in enumerate(files):
        head=True
        num=True
        THS=''
        NUM=''
        TAIL=''
        for el in f:
            if 48<=ord(el)<=57:
                head=False
            if head and 65<=ord(el)<97:
                THS+=chr(ord(el)+(97-65))
            elif head:
                THS+=el
            elif num:
                #print(el,ord(el))
                if ord(el)<48 or ord(el)>57:
                    num=False
                    TAIL+=el
                    continue
                NUM+=el
            else:
                if 65<=ord(el)<97:
                    TAIL+=chr(ord(el)+(97-65))
                else:
                    TAIL+=el
        #print(THS,NUM,TAIL)
        file[idx]= (THS,int(NUM), idx)
    file.sort()
    print(file)
                    
                
                
    answer=[]
    for a,b, t in file:
        answer.append(new[t])
  
    #print(answer)
                
                
    #print(ord('9'), ord('0'))
    
    return answer