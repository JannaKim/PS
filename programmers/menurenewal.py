#import sys; sys.setrecursionlimit(10000)
mx=[ 2 for _ in range(11)]
ans=[[] for _ in range(11)]
customer=0 # customer num
Lcourse=0 # longest course
isOrdered= [[False]*26 for _ in range(21)] # check if current customer ordered this menu
exists= [False]*26 # 이 알파벳이 메뉴에 있는지
coursecopy=[] # course 배열 그대로 카피
def exSearch(i, cnt, case, changed):
    #print(i, cnt, case)
    global Lcourse
    if (25-i+1)+cnt<2: return
    if cnt>Lcourse: return
    global customer
    global mx
    global ans
    global exists
    global coursecopy

    if changed and cnt in coursecopy:
        commonly_liked=0
        for j in range(customer):
            found=True
            for el in case: # 현재문자열 가진 손님 명수 구하기
                if not isOrdered[j][ord(el)-65]:
                    found=False
                    break
            if found:
                commonly_liked+=1
        
        if mx[cnt]==commonly_liked:
            ans[cnt].append(case)

        elif mx[cnt]<commonly_liked:
            ans[cnt]=[case]
            mx[cnt]= commonly_liked # dk dlrjf?
            
        
    if i==26 or cnt==Lcourse: return # 알파벳 26개니까 인덱스 25까지 봄 현재껄 선택해야하니까  
    exSearch(i+1, cnt, case, False)
    if exists[i]:
        case+=chr(i+65)
        exSearch(i+1, cnt+1, case, True) # check validity if changed= True


def solution(orders, course):
    global customer
    global isOrdered
    global Lcourse
    customer= len(orders)
    Lcourse= max(course)
    global ans
    global mx
    global exists
    global coursecopy
    coursecopy= [el for el in course]

    for i, order in enumerate(orders):
        for menu in order:
            isOrdered[i][ord(menu)-65]=True
            exists[ord(menu)-65]=True


    exSearch(0, 0, '', False)
    answer = []
    for i in course:
        for el in ans[i]:
            answer.append(el)
    answer.sort()
             
    return answer

#print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))

#print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))

#['CDE', 'ADE', 'ACE', 'ACD'] 3
#['ACDE'] 4

#print(2**26)
#print(solution(["ABC", "ABC", "ABC", "DE", "FG"], [2,3]))

