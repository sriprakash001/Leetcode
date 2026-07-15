class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = n**2
        even = (n+1)*n
        while even != 0:
            odd ,even = even , odd % even
        return odd