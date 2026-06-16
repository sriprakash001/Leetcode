class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for i in s:
            if i.isalpha():
                res.append(i)
            elif res and i == '*':
                res.pop()
            elif i == '#':
                res.extend(res)
            elif i == '%':
                res.reverse()
        return "".join(res)