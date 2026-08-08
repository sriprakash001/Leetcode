class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch,0)+1
        
        # find the char that occurs less than 3 times
        for i in dic:
            if dic[i] < k:
                parts = s.split(i) # for example 1: ["aaa",""]

                answers = []
                for part in parts:
                    result = self.longestSubstring(part, k)
                    answers.append(result)
                return max(answers)

        return len(s)