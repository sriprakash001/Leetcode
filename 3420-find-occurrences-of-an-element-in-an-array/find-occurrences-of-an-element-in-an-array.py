class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        pos = []
        for index,num in enumerate(nums):
            if num == x:
                pos.append(index)
        
        ans = []
        for i in queries:
            if i <= len(pos):
                ans.append(pos[i-1])
            else:
                ans.append(-1)
        return ans