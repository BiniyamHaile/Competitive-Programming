class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        fib_1 = 0
        fib_2 = 1
        for i in range(n-1):
            temp = fib_1
            fib_1 = fib_2
            fib_2 = temp + fib_1
        return fib_2
            
            