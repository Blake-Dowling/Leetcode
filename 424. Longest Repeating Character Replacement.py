class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        curChars = dict()
        maxLength = 0
        while right < len(s):
            curChar = s[right]
            curChars[curChar] = curChars.get(curChar, 0) + 1
            right += 1
            #if <= k replaceable (non-majority) characters 
            if (right - left) - max(curChars.values()) <= k:
                maxLength = max(maxLength, right - left)
            else:
                leftChar = s[left]
                curChars[leftChar] -= 1
                if curChars[leftChar] == 0:
                    del curChars[leftChar]
                left += 1
        return maxLength
