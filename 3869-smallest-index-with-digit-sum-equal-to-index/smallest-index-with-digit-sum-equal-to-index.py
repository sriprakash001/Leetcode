class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            summ = 0
            while n > 0:
                summ += n % 10
                n = n // 10
            if summ == i:
                return i
        return -1

