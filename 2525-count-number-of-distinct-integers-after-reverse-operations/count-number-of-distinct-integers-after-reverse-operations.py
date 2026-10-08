class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        ans = set(nums)
        for i in nums:
            rev = 0
            while i > 0:
                n = i % 10
                rev = rev * 10 + n
                i = i // 10
            ans.add(rev)
        return len(ans)