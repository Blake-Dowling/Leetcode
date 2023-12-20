class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k % nums.size();
        int tempSize = (nums.size()-k) * sizeof(int);
        int* tempArray = (int*)malloc(tempSize);
        memcpy(tempArray, &nums[0], tempSize); //beginning to temp
        memmove(&nums[0], &nums[nums.size()-k], k * sizeof(int)); //move left
        memcpy(&nums[k], tempArray, tempSize); //temp to end
    }
};