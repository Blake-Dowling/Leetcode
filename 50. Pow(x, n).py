class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1/x
            n = -n
        res = self.myPow(x, int(n/2))
        res *= res
        if n % 2 == 1:
            res *= x
        return res

