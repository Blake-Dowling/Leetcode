class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curChars = dict()
        left = 0
        right = 0
        maxLength = 0
        while right < len(s):
            if s[right] not in curChars:
                curChars[s[right]] = 1
                right += 1
                maxLength = max(maxLength, right-left)
            else:
                del curChars[s[left]]
                left += 1
        return maxLength
        