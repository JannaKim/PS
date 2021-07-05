#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    vector<vector<int>> ans;
    vector<vector<pair<int, int>>> dp;
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
        for(int ths = 0; ths <= target; ++ths){
            vector<pair<int, int>> tmp;
            dp.push_back(tmp);
        }
        sort(candidates.begin(), candidates.end());
        
        int n = candidates.size();
        for(int ths = 0; ths < candidates.size(); ++ths){
            for(int i = 0; i < target; ++i){
                if((i == 0) && (candidates[ths] + i <= target)){
                    dp[candidates[ths] + i].push_back({i, candidates[ths]});
                }
                else if((dp[i].size() > 0) && (candidates[ths] + i <= target)){
                    dp[candidates[ths] + i].push_back({i, candidates[ths]});
                }
            }
        }
        
        
        for(int i = 0; i < dp[target].size(); ++i){
            vector<int> stc;
            stc.clear();
            stc.push_back(dp[target][i].second);
            dfs(dp[target][i].first, stc);
        }
        return ans;
    }
    
    void dfs(int loc, vector<int>& stc){
        if(loc == 0) {ans.push_back(stc); return;}
        for(int i = 0; i < dp[loc].size(); ++i){
            if(dp[loc][i].second<=stc.back()){
            stc.push_back(dp[loc][i].second);
            dfs(dp[loc][i].first, stc);
            stc.pop_back();
            }
        }
        
        return;
    }
};

void print(vector<vector<int>> v){
    for(int i = 0; i < v.size(); ++i){
        for(int j = 0; j < v[i].size(); ++j){
        cout << v[i][j]<< " ";
    }
    cout<<"\n";
    }

}
int main(){
    Solution sol;
    vector<int> example{2,3,6,7};
    vector<vector<int>> v;
    v = sol.combinationSum(example, 7);
    print(v);
}


/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Combination Sum.
Memory Usage: 12.2 MB, less than 50.56% of C++ online submissions for Combination Sum.
*/