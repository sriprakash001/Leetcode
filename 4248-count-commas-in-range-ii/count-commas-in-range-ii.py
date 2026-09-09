class Solution:
    def countCommas(self, n: int) -> int:
        state = 1000
        count = 0
        while n >= state:
            count  += (n-state+1)
            state *= 1000
        return count