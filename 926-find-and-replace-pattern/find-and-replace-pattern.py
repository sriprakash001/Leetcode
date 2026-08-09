class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            def count_pattern(s1,s2):
                mapping = {}
                mapped = {}
                for a,b in zip(s1,s2):
                    if a in mapping and mapping[a] != b:
                        return False
                    elif b in mapped and mapped[b] != a:
                        return False
                    mapping[a] = b
                    mapped[b] = a
                return True
            x = count_pattern(word,pattern)
            if x:
                ans.append(word)
        return ans
