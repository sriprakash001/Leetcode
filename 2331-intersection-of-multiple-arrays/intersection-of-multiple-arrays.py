class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = {}
        for i in nums:
            for j in set(i):
                count[j] = count.get(j,0)+1
        ans = []
        for i in count:
            if count[i] == len(nums):
                ans.append(i)
        return sorted(ans)