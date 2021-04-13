def solution(record):
    ans = []
    dic={}
    for line in record:
        if line.split()[0]=='Leave':
            ans.append([line.split()[1],"님이 나갔습니다."])
            continue

        command, ID, nickname = line.split()
        if command=='Change':
            dic[ID]=nickname
            continue
        if ID not in dic:
            dic[ID]=nickname
            ans.append([ID,"님이 들어왔습니다."])
        else:
            dic[ID]=nickname
            ans.append([ID,"님이 들어왔습니다."])

        
    answer=[]

    for id_, el in ans:
        answer.append(dic[id_]+el)
    return answer


print(solution(	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))