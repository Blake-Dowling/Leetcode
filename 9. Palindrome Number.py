class Solution:
    def isPalindrome(self, x: int) -> bool:
        while True:
            #Base - negative or 1 digit
            if x < 0:
                return False
            if x < 10:
                return True
            #Compare first and last
            first = int(x / (10 ** int(log10(x))))
            last = int(x % 10)
            if first != last:
                return False
            #Remove first and last
            firstWithSig = first * (10 ** int(log10(x)))
            numZeros = int(log10(x)) - int(log10(x - firstWithSig)) - 1
            x = x - firstWithSig
            x = int(x / 10)
            #Handle zeros
            while numZeros > 0:
                last = int(x % 10)
                if last != 0:
                    return False
                x = int(x / 10)
                numZeros -= 1
        return False
