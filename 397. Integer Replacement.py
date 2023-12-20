class Solution:
    # 1, 2,  3,   4,  5,  6, 7, 8, 9
    # 0, 1/, 2-, 2//, 3-, 3


    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(int(n/2)) + 1
        else:
            return min(self.integerReplacement(n-1), self.integerReplacement(n+1)) + 1


    # def integerReplacement(self, n: int) -> int:
    #     steps = [0 for i in range(n+2)]
    #     steps[2] = 1
    #     i = 2
    #     while i <= n - 1:
    #         i += 2
    #         steps[i] = steps[int(i/2)] + 1
    #         steps[i-1] = min(steps[i-2], steps[i]) + 1
    #     return steps[n]