class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i >= 0:
            newVal = (digits[i] + carry) % 10
            carry = int((digits[i] + carry) / 10)
            digits[i] = newVal
            i -= 1
        if carry > 0:
            return [carry] + digits
        return digits
