#include <string>
#include <iostream>
using namespace std;

string v = " AEIOU";
string w;
int ans = -1;

bool dfs(int depth, string occ); // occurence

int solution(string word) {
    w = word;
    string vacant = "";
    dfs(0, vacant);
    return ans;
}
bool compare(string occ){
    ++ans;
    if(occ == w) return true;
    return false;
}

bool dfs(int depth, string occ){
    if(depth == 6) return false;
    
    if(compare(occ)) return true;
    
    for(int i = 1; i < 6; ++i){
        occ.push_back(v[i]);
        if(dfs(depth + 1, occ)) return true;
        occ.pop_back();
    }
    return false;
}