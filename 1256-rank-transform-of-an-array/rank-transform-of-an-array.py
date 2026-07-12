class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(set(arr))
        d = {}
        rank = 1
        for i in a:
            d[i] = rank
            rank +=1
        return [ d[i] for i in arr]

        