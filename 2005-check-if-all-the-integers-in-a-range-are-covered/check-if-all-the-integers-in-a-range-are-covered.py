class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left,right+1):
            default = False
            for start , end in ranges:
                if start <= num <= end:
                    default = True
                    break
            if not default:
                return False
        return True