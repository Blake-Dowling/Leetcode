class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        while i < len(nums):
            if nums[i] == nums[i-2]:
                nums.pop(i)
                i -= 1
            i += 1

