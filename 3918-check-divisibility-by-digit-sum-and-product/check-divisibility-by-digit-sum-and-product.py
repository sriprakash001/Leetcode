class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        for digit in str(n):
            digit = int(digit)
            s += digit
            p *= digit

        return n % (s + p) == 0