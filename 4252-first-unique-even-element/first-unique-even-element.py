from collections import Counter
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        dic = Counter(nums)
        for i in nums:
            if i%2==0:
                if dic[i] == 1:
                    return i
        return -1
        