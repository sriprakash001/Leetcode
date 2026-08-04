class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums1 = set(nums)
        ans = []
        for i in range(min(nums),max(nums)+1):
            if i not in nums1:
                ans.append(i)
        return ans