__author__ = 'phred'


class Fibonacci:

    def fib(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            self.fib(n-1) + self.fib(n-2)

    def two(self, a):
        return a * a

    def three(self):
        return self.two(23)