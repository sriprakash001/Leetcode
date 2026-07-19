class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        s=list(set(word1))
        c=list(set(word2))
        for i in s:
            h=word1.count(i)
            m=word2.count(i)
            n=abs(h-m)
            if(n>3):
                return False
        for i in c:
            h=word1.count(i)
            m=word2.count(i)
            n=abs(h-m)
            if(n>3):
                return False
        return True
