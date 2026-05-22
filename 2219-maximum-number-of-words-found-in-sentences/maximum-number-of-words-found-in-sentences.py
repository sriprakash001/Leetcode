class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for i in sentences:
            word = i.split()
            count = 0
            for j in word:
                count +=1
            max_count = max(count,max_count)
        return max_count