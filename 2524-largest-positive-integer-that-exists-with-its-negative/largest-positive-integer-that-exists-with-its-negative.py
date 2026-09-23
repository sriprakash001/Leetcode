class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        maxx = -1
        nums = set(nums)
        for i in nums:
            if i > maxx and -i in nums:
                maxx = i
        return maxx