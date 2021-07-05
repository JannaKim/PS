class Solution {
private:
    bool H[(int)(1e5) + 10];
public:
    int findDuplicate(vector<int>& nums) {
        fill(&H[0], &H[(int)(1e5) + 10], false);
        int n = nums.size();
        for(int i = 0; i < n + 1; ++i){
            if(H[nums[i]] == true) return nums[i];
            H[nums[i]] = true;
        }
        return -1;
    }
};
/*
Runtime: 92 ms, faster than 91.47% of C++ online submissions for Find the Duplicate Number.
Memory Usage: 61.3 MB, less than 59.31% of C++ online submissions for Find the Duplicate Number.

class Solution {

public:

int findDuplicate(vector<int>& nums) {
    int n=nums.size()-1;
    int low=1;
    int high=n;
    int mid;
    while(low<high){
        mid=(low+high)/2;
        int count=0;
        for(int num:nums){
            if(num<=mid) count++;
        }
        if(count>mid) high=mid;
        else low=mid+1; 
    }
    return low;
}
};

*/