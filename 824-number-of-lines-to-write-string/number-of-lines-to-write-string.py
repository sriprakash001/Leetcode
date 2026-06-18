class Solution(object):
    def numberOfLines(self, widths, s):
        ans = [0, 0]
        n = len(s)
        if n == 0:
            return ans
        sum_width = 0
        ans[0] = 1
        for char in s:
            temp = widths[ord(char) - ord('a')]
            if temp + sum_width <= 100:
                sum_width += temp
            else:
                ans[0] += 1
                sum_width = temp
        ans[1] = sum_width
        return ans 