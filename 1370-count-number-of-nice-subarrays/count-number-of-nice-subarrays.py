class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd = 0
        l = 0
        m = 0
        for r in range(len(nums)):
            if nums[r] % 2:#odd number return something so can't be 0 so thats where we increse odd
                odd += 1

            while odd > k:
                if nums[l] % 2 :
                    odd -= 1
                l += 1
                m = l
            
            if odd == k:
                while not nums[m] % 2: # here we increase the m until it meets the first odd number 
                    m += 1
                count += (m-l)+1
        return count