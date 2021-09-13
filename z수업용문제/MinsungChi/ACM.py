a= int(input())
for  i in range(0,a):
    h, w, n = map(int, input().split())
    an=0
    an+=((n%h)+1)*100
    an+=((n//h)+1)    

print(an)