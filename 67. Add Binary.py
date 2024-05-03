class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry >= 1:
            sum = carry
            if i >= 0:
                sum += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                sum += ord(b[j]) - ord('0')
                j -= 1
            result += str(sum % 2)
            carry = int(sum / 2)
        #Reverse result O(n)
        return result[::-1]