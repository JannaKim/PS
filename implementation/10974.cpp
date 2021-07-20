#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

vector <int> v;
int H[10];
int n;
void backtrack(int cnt){
    if(cnt == n){
        for(auto it : v) cout<<it<<" ";
        cout<<"\n";
        return;
    }
    for(int i = 0; i < n; ++i){
        if(H[i] == false){
            H[i] = true;
            v.push_back(i + 1);
            backtrack(cnt + 1);
            H[i] = false;
            v.pop_back();
        }
        
    }

}
int main(){
    fill(&H[0], &H[9], false);
    scanf("%d", &n);
    backtrack(0);
}