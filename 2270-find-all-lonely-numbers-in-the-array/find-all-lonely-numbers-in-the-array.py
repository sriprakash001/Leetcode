from collections import Counter
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [n for n in nums if count[n]==1 and count[n-1] + count[n+1]==0]