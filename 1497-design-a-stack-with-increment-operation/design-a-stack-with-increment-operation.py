class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = []
        self.max_size = maxSize
    def push(self, x: int) -> None:
        if len(self.stk) < self.max_size:
            self.stk.append(x)
    def pop(self) -> int:
        if not self.stk:
            return -1
        else:
            s = self.stk.pop()
            return s
    def increment(self, k: int, val: int) -> None:
        # chk the k 
        k = min(k,len(self.stk))
        for i in range(k):
            self.stk[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)