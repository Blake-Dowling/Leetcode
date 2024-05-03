class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numCount = dict()
        for n in nums:
            numCount[n] = numCount.get(n, 0) + 1
        for n in numCount.keys():
            if numCount[n] == 1:
                return n
        return -1