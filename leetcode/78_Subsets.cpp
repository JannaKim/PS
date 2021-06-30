#include <iostream>
#include <string>
#include <stdio.h>
#include <queue>
#include <vector>
using namespace std;

class Solution {
private: 
    vector<vector<int>> ans;
    vector<int> stc;
    int n;
    
public:
    void backtrack(int idx, vector<int>& nums){
        if(idx == n){
            ans.push_back(stc);
            return;
        }
        backtrack(idx + 1, nums);
        stc.push_back(nums[idx]);
        backtrack(idx + 1, nums);
        stc.pop_back();
        
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        n = nums.size();
        stc.clear();
        backtrack(0, nums);
        return ans;
    }   
};