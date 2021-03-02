def solution(numbers, hand):
    left_finger_loc = 4
    right_finger_loc = 4
    answer= ''
    l_middle = False
    r_middle = False
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left_finger_loc = i//3+1
            l_middle = False
        elif i in [3, 6, 9]:
            answer +='R'
            right_finger_loc = i//3
            r_middle = False
        else:
            if (i+1)//3 !=0: # 0이 아닐 때
                floor = (i+1)//3
                if hand == 'left':
                    if abs(floor-left_finger_loc) <= abs(floor-right_finger_loc):
                        left_finger_loc = floor
                        answer +='L'
                        l_middle = True
                    else:
                        if l_middle == True and abs(floor-left_finger_loc)==1:
                            left_finger_loc = floor
                            answer +='L'
                            l_middle = True
                        else:
                            right_finger_loc = floor
                            answer +='R'
                            r_middle = True
                else:
                    if abs(floor-left_finger_loc) >= abs(floor-right_finger_loc):
                        right_finger_loc = floor
                        answer +='R'
                        r_middle = True
                    else:
                        if r_middle == True and abs(floor-right_finger_loc)==1:
                            right_finger_loc = floor
                            answer +='R'
                            r_middle = True
                        else:
                            left_finger_loc = floor
                            answer +='L'
                            l_middle = True
            else: # 0일 때
                floor = 4
                if hand == 'left':
                    if abs(floor-left_finger_loc) <= abs(floor-right_finger_loc):
                        left_finger_loc = 4
                        answer +='L'
                        l_middle = True
                    else:
                        right_finger_loc = 4
                        answer +='R'
                        r_middle = True
                else:
                    if abs(floor-left_finger_loc) >= abs(floor-right_finger_loc):
                        right_finger_loc = 4
                        answer +='R'
                        r_middle = True
                    else:
                        left_finger_loc = 4
                        answer +='L'
                        l_middle = True


                        
                        
                    
            
            
    
    return answer

L = [int(i) for i in input().split()]
hand = input()
print(solution(L, hand))

'''
1 3 4 5 8 2 1 4 5 9 5
right

7 0 8 2 8 3 1 5 7 6 2
left

1 2 3 4 5 6 7 8 9 0
right

'''