class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_counter = {}
        normal_str = "".join(ch.lower() if ch.isalnum() else ' ' for ch in paragraph)
        
        for i in normal_str.split():
            if i not in banned:
                word_counter[i] = word_counter.get(i,0)+1

        cur_max = 0
        ans = ""
        for i in word_counter:
            if word_counter[i] > cur_max:
                cur_max = word_counter[i]
                ans = i
        return ans