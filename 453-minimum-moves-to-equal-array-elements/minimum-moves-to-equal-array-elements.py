class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minelement = min(nums)
        targetsum = len(nums) * minelement
        totalsum = sum(nums)
        return totalsum-targetsum