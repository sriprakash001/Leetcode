class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            a = i
            left = i+1
            right = n-1
            while left < right:
                currsum = nums[a] + nums[left] + nums[right]
                if abs(currsum-target) < abs(closest-target):
                    closest = currsum
                elif currsum < target:
                    left += 1
                elif currsum > target:
                    right -= 1
                else:
                    return currsum
        return closest