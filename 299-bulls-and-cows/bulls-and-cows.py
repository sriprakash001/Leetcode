from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        count = {}
        for s,g in zip(secret,guess):
            if s == g:
                bull += 1
            else:
                if count.get(s,0) < 0:
                    cow += 1
                if count.get(g,0) > 0:
                    cow += 1
                count[s] = count.get(s,0) + 1
                count[g] = count.get(g,0) - 1
        return f"{bull}A{cow}B"

        