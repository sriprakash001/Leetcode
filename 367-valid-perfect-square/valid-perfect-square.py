class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        while l <= num:
            if l*l < num:
                l += 1
            elif l*l == num:
                return True
            else:
                return False  