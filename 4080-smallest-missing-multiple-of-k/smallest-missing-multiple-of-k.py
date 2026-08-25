class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            if nums[0] == k:
                return k *2
            return k 
        ans = []
        for i in range(1,len(nums)+k+1):
            ans.append(i*k)
        for i in ans:
            if i not in nums:
                return i