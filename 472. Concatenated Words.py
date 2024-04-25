class Solution:
    def __init__(self):
        self.wordMap = dict()
    def wordIsConcat(self, word: str) -> bool:
        if len(word) == 0:
            return True
        left = 0
        right = 0
        #O(k^2)
        while right < len(word):
            if word[left:right+1] in self.wordMap:
                if(self.wordIsConcat(word[right+1:])):
                    return True
            right += 1
        return False

    #Time: O(n*k^2)
    #Space: O(n)
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        for word in words: #O(n)
            self.wordMap[word] = 1
        result = []
        for word in words: #O(n)
            del self.wordMap[word]
            if self.wordIsConcat(word): #O(k^2)
                result.append(word)
            self.wordMap[word] = 1
        return result