from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = Counter(nums)
        max_ = max(dic.values())
        count = 0
        # for i in dic.values():
        #     if i > max_:
        #         max_ = i
        for i in dic.values():
            if i == max_:
                count += max_
        return count
        