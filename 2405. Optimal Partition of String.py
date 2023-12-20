class Solution:
    def partitionString(self, s: str) -> int:
        i = 0
        groups = [[]]
        while i < len(s):
            if s[i] in groups[-1]:
                groups.append([])
            groups[-1].append(s[i])
            i+=1
        return len(groups)