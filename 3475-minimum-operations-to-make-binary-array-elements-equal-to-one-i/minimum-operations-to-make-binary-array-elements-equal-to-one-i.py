class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count=0
        for i in range(n-2):
            if nums[i] == 0:
                for j in range(i,i+3):
                    nums[j] = 1-nums[j]
                count +=1
        for i in nums:
            if i==0:
                return -1
        return count
        