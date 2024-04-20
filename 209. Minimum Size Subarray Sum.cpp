class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int minK = INT_MAX;
        int left = 0;
        int right = 0;
        int curSum = 0;

        while(true){
            while(curSum < target && right < nums.size()){
                curSum += nums[right];
                right ++;
            }
            if(right >= nums.size() && curSum < target){
                break;
            }
            minK = min(minK, right-left);
            curSum -= nums[left];
            left ++;
        }
        if(minK == INT_MAX){
            minK = 0;
        }
        return minK;
    }
};