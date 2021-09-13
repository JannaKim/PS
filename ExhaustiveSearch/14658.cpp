#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct loc{
    int y, x;
};
vector <loc> star;
int bruteforce();
bool bounce(int &ly, int &lx, int y, int x);
int n, m, l, k;

int main(){
    
    cin >> n >> m >> l >> k;
    star.resize(k);
    for(int i = 0; i < k; ++i){
        cin >> star[i].y >> star[i].x;
    }
    int ans = bruteforce();
    cout << ans;
}

void printvec(vector <int> v){
    for(auto it : v) cout << it << " ";
    cout << "\n";
}

int bruteforce(){
    int ans = 100;
    int y, x, cy, cx;
    int mx = 0;
    for(int i = 0; i < k; ++i){
        y = star[i].y;

        for(int j = 0; j < k; ++j){
            x = star[j].x;
            // printvec({y, x});

            int cnt = 0;
            for(int h = 0; h < k; ++h){
                cy = star[h].y;
                cx = star[h].x;
                if(bounce(y, x, cy, cx)) cnt += 1;
            }
            ans = min(ans, k -cnt);
        }
    }
    return ans;
}

void print(int x){
    cout << x << "\n";
}

bool bounce(int &ly, int &lx, int y, int x){
    if(y < ly || x < lx) return false;
    if(y > ly + l || x > lx + l) return false;
    return true;
}