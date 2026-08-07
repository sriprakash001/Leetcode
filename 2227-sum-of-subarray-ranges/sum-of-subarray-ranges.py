class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        
        def sum_subarray_max():
            stack = []
            result = 0
            for i in range(n+1):
                while stack and ( i == n or nums[stack[-1]] < nums[i] ) :
                    mid = stack.pop()
                    left = mid - stack[-1] if stack else mid + 1
                    right = i- mid
                    result += nums[mid]*left*right
                stack.append(i)
            return result
        
        def sum_subarray_min():
            stack = []
            result = 0
            for i in range(n+1):
                while stack and ( i == n or nums[stack[-1]] > nums[i] ):
                    mid = stack.pop()
                    left = mid - stack[-1] if stack else mid + 1
                    right = i- mid
                    result += nums[mid]*left*right
                stack.append(i)
            return result
        return sum_subarray_max() - sum_subarray_min()