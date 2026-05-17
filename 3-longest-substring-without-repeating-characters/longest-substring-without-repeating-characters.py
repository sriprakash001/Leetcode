class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set = set()
        res = 0
        left = 0
        for right in range(len(s)):
            while s[right] in res_set:
                res_set.remove(s[left])
                left +=1
            res_set.add(s[right])
            res = max(res,right-left+1)
        return res