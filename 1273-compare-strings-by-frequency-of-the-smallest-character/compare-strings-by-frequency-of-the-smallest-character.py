class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def freq(s):
            smallest = min(s)
            count = 0
            for ch in s:
                if ch == smallest:
                    count +=  1
            return count
        ans = []
        for q in queries:
            qFreq = freq(q)
            count = 0
            for w in words:
                wFreq = freq(w)
                if qFreq <  wFreq:
                    count += 1
            ans.append(count)
        return ans