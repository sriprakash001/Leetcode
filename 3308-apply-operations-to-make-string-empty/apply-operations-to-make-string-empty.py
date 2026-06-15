from collections import Counter
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq = Counter(s)
        mx = max(freq.values())
        ans = []
        for i in range(len(s)-1,-1,-1):
            if freq[s[i]] == mx:
                ans.append(s[i])
                freq[s[i]] = 0
        return "".join(reversed(ans))
        