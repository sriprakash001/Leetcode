class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        dic = {}
        for i in range(len(nums)-k+1):
            seen = set()
            for j in range(i,i+k):
                seen.add(nums[j])
            for j in seen:
                dic[j] = dic.get(j,0)+1
        ans = []
        for i in dic:
            if dic[i] == 1:
                ans.append(i) 
        return max(ans) if ans else -1