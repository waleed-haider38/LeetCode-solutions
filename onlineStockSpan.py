class StockSpanner:

    def __init__(self):
        # Stack will store pairs:
        # (stock_price, span)
        self.stack = []

    def next(self, price: int) -> int:

        # Current day's span starts with 1
        span = 1

        # Remove all previous prices that are
        # less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:

            # Add their span to current span
            span += self.stack[-1][1]

            # Remove the processed element
            self.stack.pop()

        # Store current price and its span
        self.stack.append((price, span))

        # Return the span for current day
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# print(obj.next(100))  # 1
# print(obj.next(80))   # 1
# print(obj.next(60))   # 1
# print(obj.next(70))   # 2
# print(obj.next(60))   # 1
# print(obj.next(75))   # 4
# print(obj.next(85))   # 6