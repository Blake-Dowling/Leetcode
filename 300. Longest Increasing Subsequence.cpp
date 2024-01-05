class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> longest = vector<int>(nums.size(), 1);
        int i = nums.size() - 1;
        while(i >= 0){
            
            int j = nums.size() - 1;
            while(j > i){
                // cout << nums[j];
                if(nums[j] > nums[i] && 1 + longest[j] > longest[i]){
                    longest[i] = 1 + longest[j];
                }
                j --;
            }
            i --;
        }
        int longestVal = 1;
        for(int i = 0; i < longest.size(); i ++){
            if(longest[i] > longestVal){
                longestVal = longest[i];
            }
        }
        return longestVal;
    }
};