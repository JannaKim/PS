#include <stdio.h>
#include <vector>
#include <string>
#include <stdlib.h>
using namespace std;
int main(){ //컴파일 언어: 시작점을 갖고있다.
//컴파일 언어는 텍스트 형태의 소스코드를 컴파일해 기계어 형태로 된 실행파일(binary)을 만들어낸다.
//실행파일은 CPU에서 바로 싱행되지 깨문에 속도가 빠르고 간결하다.
int a, b, c;
scanf("%d\n%d\n%d",&a,&b,&c);
long X = (long)a*b*c;

string s= to_string(X);
int info[10]= {0, };
for(int i=0;i<s.length();i++)
    info[s[i]-'0']+=1;

for(int i=0;i<10;i++)
    printf("%d\n",info[i]);

}