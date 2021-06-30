#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

int main(){
    //printf("%d %d", '1', '0');
    string inp;
    cin >>inp;
    int H[10] = {0, };
    for(int i = 0; i< inp.size(); ++i){
        H[ inp[i]-48 ] +=1;
    }
    int _69 = H[6] + H[9];
    if(_69 % 2 ==1){//odd
        _69>>=1;
        _69++;
    }
    else _69>>=1;
    H[6] = _69;
    H[9] = _69;
    int ans = 0;
    for(int i = 0; i < 10; i ++){
        if(H[i] > ans) ans = H[i];
    }

    printf("%d", ans);

}