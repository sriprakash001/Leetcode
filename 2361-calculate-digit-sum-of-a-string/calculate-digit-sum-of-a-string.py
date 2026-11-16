class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = []
            for i in range(0,len(s),k):
                total = 0
                for ch in s[i:i+k]:
                    total += int(ch)
                res.append(str(total))
            s = "".join(res)
        return s
