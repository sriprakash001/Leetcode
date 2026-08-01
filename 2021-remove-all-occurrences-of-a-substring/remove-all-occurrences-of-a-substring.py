class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)
        for ch in s:
            stack.append(ch)
            if len(stack) >= m and ''.join(stack[-m:])== part: # to check last char equal to part or not 
                for i in range(m):
                    stack.pop()
        return "".join(stack)
        
        # Another approch
        # while part in s:
        #     s = s.replace(part,"",1)
        # return s

