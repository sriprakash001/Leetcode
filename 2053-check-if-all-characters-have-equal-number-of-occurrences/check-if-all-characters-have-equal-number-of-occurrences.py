from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        left = 0
        right = 1
        s1 = list(set(s))
        while right < len(count):
            if count[s1[left]] != count[s1[right]]:
                return False
            right += 1
        return True
        