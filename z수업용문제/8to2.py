import sys; input= lambda: sys.stdin.readline().rstrip()
# 8진수= 2진수 변환
s= input()
dic= {'0':'000', '1': '001', '2':'010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
'''
dic={}
dic[0]='000'
dic[1]='001'
dic[2]='010'
dic[3]='011'
dic[4]='100'
dic[5]='101'
dic[6]='110'
dic[7]='111'
'''

exe={'0':'0', '1': '1', '2':'10', '3': '11'}
'''
exe={}
exe[0]='0'
exe[1]='1'
exe[2]='10'
exe[3]='11'
'''

if s[0] in ['0', '1', '2', '3']:
    print(exe[s[0]],end='')
    s=s[1:]


for digit in s:
    print(dic[digit],end='')

