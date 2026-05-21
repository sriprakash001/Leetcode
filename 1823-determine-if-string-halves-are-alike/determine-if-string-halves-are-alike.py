class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        count = 0
        n = len(s)
        for i in range(n):
            if s[i] in vowels:
                if i < n//2:
                    count += 1
                else:
                    count -= 1
        return count == 0 
