#include <iostream>
using namespace std;

int n;

int topdown(int k);

int main(){
    cin >> n;
    int ans;
    ans = topdown(n);
    cout << ans;
}

int topdown(int k){
    if(k == 1) return 0;
    int res1 = 1e9; 
    if(k >= 3) // ?
        res1 = topdown(k / 3) + (k % 3) + 1;
    int res2 = topdown(k / 2) + (k % 2) + 1;
    if(res1 <= res2) cout << k/3 <<'<'<<k/2<<'\n';
    else cout << k/2 <<'<'<<k/3<<'\n';
    return res1 < res2 ? res1 : res2;
}