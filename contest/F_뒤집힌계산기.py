L = [0]+list(map(int, input().split()))
op = ['', '+', '-', '*', '/']
dic={}
for i in range(1,5):
    dic[L[i]]=op[i]
s = input()
#print(s)

seq=['',False,False,False,False]
for i in range(1,5):
    if dic[i] in s:
        seq[i]=True
#print(dic)
for k in range(4,0,-1):
    if seq[k]==True:
        ans=''
        while s[::-1].find(dic[k])!=-1:
            split_idx=len(s)-1-s[::-1].find(dic[k])
            #print(f'split_idx {split_idx}' )
            aidx=0
            bidx=0
            for i in range(split_idx-1, -1,-1):
                if ord(s[i])>=48:
                    aidx=i
                else:
                    break
            for i in range(split_idx+1, len(s)):
                if ord(s[i])>=48:
                    bidx=i
                else:
                    break
            #print(f'aidx {aidx} bidx {bidx}')
            if dic[k]=='*' or dic[k]=='+':
                #print(dic[k],'중')
                A = s[aidx:split_idx].replace('=','-')
                B = s[split_idx+1:bidx+1].replace('=','-')
                #print(A, B)
                mid = eval(str(int(A))+dic[k]+str(int(B)))
                #print(f'  = {mid}')
                if mid<0:
                    mid = '='+str(-mid)
                ans = s[:aidx]+str(mid)+s[bidx+1:]
            elif dic[k]=='-':
                #print(dic[k],'중')
                A = s[aidx:split_idx].replace('=','-')
                B = s[split_idx+1:bidx+1].replace('=','-')
                #print(B, A)
                mid = eval(str(int(B)) +dic[k]+ str(int(A)))
                #print(f'  = {mid}')
                if mid<0:
                    mid = '='+str(-mid)
                ans = s[:aidx]+str(mid)+s[bidx+1:]
            else:
                #print(dic[k],'중')
                A = s[aidx:split_idx].replace('=','-')
                B = s[split_idx+1:bidx+1].replace('=','-')      
                #print(B, A)          
                mid = eval(str(int(abs(int(B)))) +'//'+ str(int(abs(int(A)))))
                #print(f'  = {mid}')
                if int(A)*int(B)>=0:
                    ans = s[:aidx]+str(mid)+s[bidx+1:]
                else:
                    ans = s[:aidx]+'='+str(mid)+s[bidx+1:]

            #print('결과:',ans)
            s=ans

print(int(s.replace('=','-')))

'''
1 2 3 4
3*2+5-5+7

13


4 3 2 1
000000000000000000000000123456789

123456789



2 3 1 4
03/02*05-01+02*90

0



2 1 3 4
1-01-001-0001

-2



1 2 3 4
001+0002-00003

2



2 1 3 4
001+0002-00003

0

'''
            

# https://www.acmicpc.net/contest/problem/551/6






'''
1 2 3 4
3*2+5-5+7
'''
