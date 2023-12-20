class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        facs = [i for i in range(1, int(n/2)+1) if n % i == 0]
        facs.append(n)
        return facs[k-1] if k-1 < len(facs) else -1

