class Solution:
    def sumAndMultiply(self, n: int) -> int:
        summ = 0
        x = ""
        for i in str(n):
            if int(i) > 0:
                x += i
                summ += int(i)
        if not x:
            return 0
        return int(x)*summ


