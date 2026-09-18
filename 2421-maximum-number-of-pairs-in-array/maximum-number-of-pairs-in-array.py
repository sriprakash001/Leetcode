from collections import Counter
class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        pairs = sum(i//2 for i in count.values())
        left = sum(i%2 for i in count.values())
        return [pairs,left]