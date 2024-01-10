#Runtime Beats 85%
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.answers = []

    def next(self, price: int) -> int:
        curSpan = 1
        while len(self.stack) and self.stack[-1] <= price:
            curSpan += self.answers.pop()
            self.stack.pop()
        self.answers.append(curSpan)
        self.stack.append(price)
        return self.answers[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)