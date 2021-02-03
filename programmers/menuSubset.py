import sys; sys.setrecursionlimit(10000)
import time
mx=[ 2 for _ in range(11)]
ans=[[] for _ in range(11)]
customer=0 # customer num
Lcourse=0 # longest course
isOrdered= [[False]*26 for _ in range(21)] # check if current customer ordered this menu
courses=[]
chk= []
def exSearch(i,changed, picked):
    #print(i, cnt, case)
    global Lcourse
    global customer
    global mx
    global ans
    

    if changed and picked in courses:
        candi=''
        cnt=0
        for alp in range(26): # 고른손님들이 골통으로 가지고 있는걸 뽑는다.
            uni=True
            for cust in range(customer):
                if chk[cust] and not isOrdered[cust][alp]: # 현재 손님 골랐고 이 손님이 이 메뉴 골랐을때
                    uni=False
                    break
            if uni: 
                candi+=chr(alp+65)
                cnt+=1
        
        if mx[cnt]==picked:
            ans[cnt].append(candi)
            
            #print(f'ans[{cnt}]: {ans[cnt]}')
            #time.sleep(5)
        elif mx[cnt]<picked:
            ans[cnt]=[candi]
            mx[cnt]= picked # dk dlrjf?
            
            #print(f'ans[{cnt}]: {ans[cnt]}')
            #time.sleep(5)
    if i==customer: return
    chk[i]=True
    exSearch(i+1, True, picked+1) # check validity if changed= True
    chk[i]=False
    exSearch(i+1, False, picked)


def solution(orders, course):
    global customer
    global isOrdered
    global Lcourse
    global chk
    global courses
    customer= len(orders)
    Lcourse= max(course)
    global ans
    chk= [False]* customer

    courses= [el for el in course]
    for i, order in enumerate(orders):
        for menu in order:
            isOrdered[i][ord(menu)-65]=True

    exSearch(0,False, 0)
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


print(solution(["ABC", "ABC", "ABC", "DE", "FG"], [2,3]))
