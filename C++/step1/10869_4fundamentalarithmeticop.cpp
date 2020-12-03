#include <iostream>
using namespace std;
int main(){
    int A, B;
    cin>>A;
    cin>>B;
    //scanf("%d %d", &a, &b);
    int quotient = (A+B)>>1;//  비트를 왼쪽에서 오른쪽으로 1비트 이동할 때마다 2로 나누는 효과


    int remainder= A&(B-1);
    cout<<A+B<<'\n'<<A-B<<'\n'<<A*B<<'\n'<<A/B<<'\n'<<A%B;
}