class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        words = set(word)
        for i in words:
            if chr(ord(i)+32) in words:
                count += 1
        return count