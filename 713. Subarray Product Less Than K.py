class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        numSub = 0
        while left < len(nums):
            right = left
            curProd = 1
            while right < len(nums):
                curProd *= nums[right]
                if curProd < k:
                    numSub += 1
                else:
                    break
                right += 1
            left += 1
        return numSub
