class Solution:
    def isHappy(self, n: int) -> bool:
        l  = []
        l.append(n)
        while n != 1:
            s = 0
            for i in str(n):
                s += int(i) *int(i)
            if s not in l:
                l.append(s)
            else:
                return False
            n = s
        return True 