class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr1 = sorted(arr)
        dic = {}
        val = 1
        for i in arr1:
            if i in dic:
                continue
            else:
                dic[i] = val
                val += 1
        return [dic[i] for i in arr]
