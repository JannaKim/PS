n, k= map(int, input().split())
num= [*map(int, list(input()))]
digit= n-k
ans=[]
start=0
while digit:
    mx=[-1,-1]
    end= (-(digit-1) if -(digit-1)<0 else n)
    for idx, el in enumerate(num[start:end]):
        if mx[1]<el:
            mx= [idx+start,el]
    ans.append(str(mx[1]))
    #print(num[start:-(digit-1)], mx)
    #print('ans',ans)
    start=mx[0]+1
    digit-=1
print(''.join(ans))
        
'''
3 2
999
//output : 9

6 2
391123
//output : 9123

6 2
436436
//output : 6436

7 3
7654321
//output : 7654

6 2
362514
//output : 6514

2 1
19
//output : 9

7 3
1231234
//output : 3234

10 4
4177252841
//output : 775841





'''
def solution(n, k):
    num= [*map(int, list(input()))]
    digit= n-k
    ans=[]
    start=0
    while digit:
        mx=[-1,-1]
        end= (-(digit-1) if -(digit-1)<0 else n)
        for idx, el in enumerate(num[start:end]):
            if mx[1]<el:
                mx= [idx+start,el]
        ans.append(str(mx[1]))
        #print(num[start:-(digit-1)], mx)
        #print('ans',ans)
        start=mx[0]+1
        digit-=1
        
    return ''.join(ans)