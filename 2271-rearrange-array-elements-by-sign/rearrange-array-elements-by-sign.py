class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        l = 0
        r = 1
        for i in nums:
            if i > 0:
                ans[l] = i
                l += 2
            if i < 0:
                ans[r] = i
                r += 2
        return ans
