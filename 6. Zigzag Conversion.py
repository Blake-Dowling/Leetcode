class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for i in range(numRows)]
        i = 0
        dirInc = 1
        r = 0
        while i < len(s):
            rows[r].append(s[i])
            if r == numRows-1:
                dirInc = -1
            if r == 0:
                dirInc = 1
            r += dirInc
            i += 1
        result = ""
        for row in rows:
            for c in row:
                result += c

        return result