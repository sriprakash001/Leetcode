from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = Counter(nums)
        max_ = max(dic.values())
        count = 0
        # for i in dic.values():
        #     if i > max_:
        #         max_ = i
        for i in nums:
            if dic[i] == max_:
                count += 1
        return count
        