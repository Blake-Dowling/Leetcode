import sys
class Solution:
    def jump(self, nums: List[int]) -> int:
        lowest = [sys.maxsize for i in range(len(nums))]
        lowest[len(lowest)-1] = 0
        for i in reversed(range(len(nums)-1)):
            for j in reversed(range(1, nums[i]+1)):
                if i+j >= len(lowest) - 1:
                    lowest[i] = 1
                else:
                    if 1 + lowest[i+j] < lowest[i]:
                        lowest[i] = 1 + lowest[i+j]
            i -= 1
        return lowest[0]