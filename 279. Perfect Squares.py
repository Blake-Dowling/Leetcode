#Beats 84.37%
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(int(sqrt(n))+1)]
        minSquares = [100000 for i in range(n+1)]
        for i in range(len(minSquares)):
            if sqrt(i) % 1 == 0:
                minSquares[i] = 1
            else:
                for s in squares[:int(sqrt(i))+1]:
                    if 1 + minSquares[i-s] < minSquares[i]:
                        minSquares[i] = 1 + minSquares[i-s]
        return minSquares[-1]
