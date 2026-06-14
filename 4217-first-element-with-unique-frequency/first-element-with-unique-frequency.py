from collections import Counter
class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        count=Counter(nums)
        freq = Counter(count.values())
        for i in nums:
            if freq[count[i]] == 1:
                return i
        return -1
        