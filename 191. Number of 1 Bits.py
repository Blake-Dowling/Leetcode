class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n > 0:
            if int(n) & 1:
                weight += 1
            n = n >> 1
        return weight