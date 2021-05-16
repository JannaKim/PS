def solution(numbers, hand):
    y1, x1= 3, 0
    y2, x2= 3, 2

    ans= []
    for num in numbers:
        num-=1
        if num==-1:
            num=10
        y, x= num//3, num%3
        if x==0: # left
            y1, x1= y, x
            ans.append('L')
        elif x==2: # right
            y2, x2= y, x
            ans.append('R')
        else:
            a= abs(y1-y)+abs(x1-x)
            b= abs(y2-y)+abs(x2-x)

            if a<b:
                y1, x1= y, x
                ans.append('L')
            elif b<a:
                y2, x2= y, x
                ans.append('R')
            else:
                if hand=='left':
                    y1, x1= y, x
                    ans.append('L')
                else:
                    y2, x2= y, x
                    ans.append('R')

    return ''.join(ans)