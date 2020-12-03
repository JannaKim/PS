#include <iostream>
using namespace std;
int main()
{
    int a, b, c;
    cin>>a;
    cin>>b;
    cin>>c;
    printf("%d\n",(a+b)%c);
    printf("%d\n",((a%c)+(b%c))%c);
    printf("%d\n",(a*b)%c);
    printf("%d\n",((a%c)*(b%c))%c);

    /*
    1000000007로 나눈 나머지 구하는 문제:
    나머지 연산자의 분배법칙 이용.
    (A-B)%M = ( ((A+M)%M) - ((B+M)%M) )%M
    음수가 나올 수 있기 때문에  M을 한번 더해준 후 나머지를 구한다.
    */
   return 0;
    
}