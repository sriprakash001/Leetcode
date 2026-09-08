class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        count = 0
        for i in range(1000,n+1):
            if i >= 1000 and i < 1000000:
                count += 1
            elif i > 1000000:
                count += 2
        return count 
