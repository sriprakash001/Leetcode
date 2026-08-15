class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        for num in arr:
            freq[num % k] += 1

        if freq[0] % 2 != 0:
            return False

        for r in range(1, k):
            if freq[r] != freq[k - r]:
                return False
        return True