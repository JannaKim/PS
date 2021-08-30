#include <iostream>
using namespace std;

int n;
int main(){
    cin >> n;
    int ans = 0;
    for(int i = 5; i <= 500; i *= 5){
        if(i <= n) ans += n/i;
    }
    cout << ans;
}