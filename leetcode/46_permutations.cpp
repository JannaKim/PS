class Solution {
private:
    vector<int> stc;
    int ed = 0;
    vector<vector<int>> ans;
    bool vis[6] = {};
    
    
public:
    
    void backtrack(int idx , vector<int>& nums){
        if(idx == ed) {
            ans.push_back(stc);
            return;
        }
        
        for(int i = 0; i < ed ; ++i){
            if(vis[i] == false){
                vis[i] = true;
                stc.push_back(nums[i]);
                backtrack(idx + 1, nums);
                vis[i] = false;
                stc.pop_back();
            }
            
        } 
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        fill(&vis[0], &vis[6], false);
        ed = nums.size();
        backtrack(0, nums);
        
        return ans;
    }
};
    