class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i] == k:
                    ans += 1
        return ans
