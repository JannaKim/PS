#include <iostream>
using namespace std;

int cnt = 0;
int f(int a){
    //3로 나누어 나머지가 2이면 -1 한다.
    //cout<<a<<" ";
    if (a>1){
        if (a%3 == 0){
            cnt++;
            //cout<<a<<" ";
            f(a/3);
        }

        else {
            if (a%2 == 0){
                cnt++;
                //cout<<a<<" ";
                f(a/2);
            }
            else {
                cnt++;
                f(--a);
            }
        }
    
    }
    else return cnt;
}
int main() {
    int n;
    cin>>n;
    f(n);
    cout<<cnt;
    return 0;
}