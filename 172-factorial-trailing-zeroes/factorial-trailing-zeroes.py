class Solution:
    def trailingZeroes(self, n: int) -> int:
        # trailing zeroes in n! = count how many factors of present
        ans = 0
        while n > 0:
            n = n // 5
            ans += n
        return ans