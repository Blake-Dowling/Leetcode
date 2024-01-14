class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = dict([])
        for num in range(max(nums)+1):
            points[num] = 0
        for num in nums:
            points[num] += num
        most = [0 for i in range(max(nums) + 1)]
        most[min(nums)] = points[min(nums)]
        for i in range(2, len(most)):
            most[i] = max(most[i-2] + points[i], most[i-1])
        return most[-1]