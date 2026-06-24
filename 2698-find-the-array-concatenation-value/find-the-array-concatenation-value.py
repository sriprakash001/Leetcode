class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left , right = 0 , len(nums)-1
        ans = 0
        while left  < right:
            ans += int(str(nums[left]) +str(nums[right]))
            left += 1
            right -= 1
        if left == right:
            ans += nums[right]
        return ans