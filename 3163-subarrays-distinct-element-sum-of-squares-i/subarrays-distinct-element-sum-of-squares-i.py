class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            seen = set()
            for j in nums[i:]:
                seen.add(j)
                ans += len(seen) ** 2
        return ans