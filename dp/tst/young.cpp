// #include <iostream>
// using namespace std;

// int cnt = 0;
// void f(int a, int cnt){
//     //3로 나누어 나머지가 2이면 -1 한다.
//     //cout<<a<<" ";
//     int case1, case2, case3;
//     case1 = 1e9;
//     case2 = 1e9;
//     case
//     if (a>1){
//         if (a%3 == 0){
//             cnt++;
//             //cout<<a<<" ";
//             case1 = f(a/3) + 1;
//         }

//         else {
//             if (a%2 == 0){
//                 cnt++;
//                 //cout<<a<<" ";
//                 case2f(a/2);
//             }
//             else {
//                 cnt++;
//                 f(--a);
//             }
//         }
    
//     }

//     return;
// }
// int main() {
//     int n;
//     cin>>n;
//     cout << f(n, 1);
//     return 0;
// }

#include <iostream>
using namespace std;

int cnt = 0;
void f(int a){
    //3로 나누어 나머지가 2이면 -1 한다.
    //cout<<a<<" ";
    if (a>1){
        if (a%3 == 0){
            cnt++;
            //cout<<a<<" ";
            f(a/3);
        }
        else {
            //cou

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
    return;
}
int main() {
    int n;
    cin>>n;
    f(n);
    cout<<cnt;
    return 0;
}
//
// Created by 김용환 on 2021/08/25.
//