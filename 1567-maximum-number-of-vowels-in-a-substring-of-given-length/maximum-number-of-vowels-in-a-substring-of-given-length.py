class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        vowel_count = 0
        max_count = 0
        # We check First three characters are vowels or not
        for i in range(0,k):
            if s[i] in vowels:
                vowel_count += 1
        max_count = vowel_count

        for right in range(k,len(s)):
            left = right-k
            
            if s[right] in vowels:
                vowel_count += 1
            if s[left] in vowels:
                vowel_count -= 1
            max_count = max(vowel_count,max_count)
            if vowel_count == k:
                return vowel_count
        return max_count



