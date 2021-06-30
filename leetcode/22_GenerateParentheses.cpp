#include <iostream>
#include <string>
#include <stdio.h>
#include <queue>
#include <vector>

using namespace std;

class Solution {
private:
    string stc = "";
    vector<string> ans;
public:
    vector<string> generateParenthesis(int n) {
        backtrack(0, 0, n);
        return ans;
    }
    
    void backtrack(int lo, int hi, int n){
        if (lo + hi == 2 * n){
            ans.push_back(stc);
            return;
        }
        if(lo < n){
            stc.push_back('(');
            backtrack(lo + 1, hi,  n);
            stc.pop_back();
        }
        
        if (lo > hi){
            stc.push_back(')');
            backtrack(lo, hi + 1,  n);
            stc.pop_back();
        }
    }
};