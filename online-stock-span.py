#my initial naive approach
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = -1

    def next(self, price: int) -> int:
        # monotonic decreasing stack
        self.i +=1

        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        
        res = self.i - self.stack[-1][0] if self.stack else self.i + 1
        self.stack.append((self.i, price))

        return res

# I tried to be a little bit better
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # monotonic decreasing stack
        pops = 0

        while self.stack and self.stack[-1][0] <= price:
            _, cur_pops = self.stack.pop()
            pops += (cur_pops + 1)

        self.stack.append((price, pops))

        return self.stack[-1][1] + 1

# A decent solution I had to look up
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # monotonic decreasing stack
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# [100, 80, 60, ]
