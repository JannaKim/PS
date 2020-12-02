heavy=[]
light=[]

poss=[True]*(13)
num=0
for _ in range(3):
    L=input().split()
    sign=L[4]
    del L[4]
    L=[int(i) for i in L]
    
    if sign=='>':
        num+=1
        heavy +=L[:4]
        light +=L[4:]
    elif sign=='<':
        num+=1
        heavy +=L[4:]
        light +=L[:4]
    else:
        for el in L:
            poss[el]=False

#print(heavy, light, poss,sep='\n')

cand=[]
if not num: # 모두 등호
    for i in range(1,13):
        if poss[i]:
            cand.append(i)
    if len(cand)==0:
        print('impossible')
    else: #elif len(cand)>=1:
        print('indefinite')

else:
    if num==1: # 등호 2개
        for el in heavy:
            if poss[el]:
                cand.append((el,'+'))
        for el in light:
            if poss[el]:
                cand.append((el,'-'))


    elif num==2: # 등호 1개
        for el in heavy:
            if poss[el]: # 확인해볼 가치 o
                if el in light: # 양쪽에 있다면 진짜 동전이다
                    poss[el]=False
                elif heavy.count(el)==2:
                    cand.append((el,'+'))
        for el in light:
            if poss[el] and light.count(el)==2:
                cand.append((el,'-'))

    else: # 부등호 세개
        for el in heavy:
            if poss[el]: # 확인해볼 가치 o
                if el in light: # 양쪽에 있다면 진짜 동전이다
                    poss[el]=False
                elif heavy.count(el)==3:
                    cand.append((el,'+'))
        for el in light:
            if poss[el] and light.count(el)==3:
                cand.append((el,'-'))

    cand=set(cand)
    cand=list(cand)
    if not cand:
        print('impossible')
    elif len(cand)==1:
        print(cand[0][0],cand[0][1],sep='')
    else:
        print('indefinite')


'''
#include <iostream>
using namespace std;

int t[3][8];
string f[13][2];

int main()
{ string res = "xxx";
  for(int w=0; w<3; w++)
  { for(int j=0; j<4; j++)
      cin >> t[w][j];
    cin >> res[w];
    for(int j=4; j<8; j++)
      cin >> t[w][j];
  }
  
  for(int c=1; c<=12; c++)
  { f[c][0]=f[c][1]="===";
    for(int w=0; w<3; w++)
    { for(int j=0; j<4; j++)
      { int c = t[w][j];
        f[c][0][w] = '<'; 
        f[c][1][w] = '>'; 
      }
      for(int j=4; j<8; j++)
      { int c = t[w][j];
        f[c][0][w] = '>'; 
        f[c][1][w] = '<'; 
      }
    }
  }
         
  int sol=0;
  int fls;
  char sgn;
  for(int c=1; c<=12; c++)
  { if(f[c][0]==res) { sol++; fls=c; sgn='-'; }
    if(f[c][1]==res) { sol++; fls=c; sgn='+'; }
  }  
           
  if(sol==1) cout << fls << sgn << endl;
  if(sol==0) cout << "impossible" << endl;     
  if(sol>=2) cout << "indefinite" << endl;     
 
  return 0;
}
'''






'''
1 2 3 10 > 4 5 6 11
1 2 3 11 > 7 8 9 10
1 4 7 10 < 2 5 8 12

4 8 10 11 = 1 2 5 7
2 4 7 12 = 8 9 10 11
3 7 10 11 > 6 8 9 12

1 4 6 10 < 5 7 9 12
2 5 4 11 > 6 8 7 10
3 6 5 12 < 4 9 8 11
'''