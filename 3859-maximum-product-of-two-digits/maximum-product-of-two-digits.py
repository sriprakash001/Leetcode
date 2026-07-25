class Solution:
    def maxProduct(self, n: int) -> int:
        mul = 0
        x = [int(i) for i in str(n)]
        for i in range(len(x)):
            for j in range(len(x)):
                if i == j:
                    continue
                elif x[i]*x[j] > mul :
                    mul = x[i]*x[j]
        return mul