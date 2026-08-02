class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        uni = []
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j]) == k and (nums[i],nums[j]) not in uni:
                    count += 1
                    uni.append((nums[i],nums[j]))
        return count
