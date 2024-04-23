class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charCount = dict()
        for c in s1:
            charCount[c] = charCount.get(c, 0) + 1
        left = -(len(s1)-1)
        right = 0
        while right < len(s2):
            charCount[s2[right]] = charCount.get(s2[right], 0) - 1
            if charCount[s2[right]] == 0:
                del charCount[s2[right]]
            if len(charCount.keys()) == 0:
                return True
            if left >= 0:
                charCount[s2[left]] = charCount.get(s2[left], 0) + 1
                if charCount[s2[left]] == 0:
                    del charCount[s2[left]]
            right +=1
            left += 1
        return False
