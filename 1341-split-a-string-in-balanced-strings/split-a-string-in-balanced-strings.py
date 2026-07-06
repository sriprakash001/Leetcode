class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        ans = 0
        for i in s:
            if i == 'R':
                balance += 1
            else: # "L" 
                balance -= 1
            if balance == 0:
                ans += 1
        return ans