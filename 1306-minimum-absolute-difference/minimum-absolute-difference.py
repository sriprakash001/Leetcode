class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:   
        arr.sort()
        if len(arr) <=2:
            return [arr]
        mini = 100000000
        for i in range(1,len(arr)):
            mini = min(mini,arr[i]-arr[i-1])
        ans = []
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] == mini:
                ans.append([arr[i-1],arr[i]])
        return ans

