from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        c = Counter(list(str(n)))
        m = 0
        for key,val in c.items():
            m += int(key) * val
        return m

        