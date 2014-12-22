from time import *
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def memo_fib(n):
    memo = [None] * (n + 1)
    def fib_helper(n, memo):
        if n == 1 or n == 2:
            memo[n] = 1
            return 1
        if memo[n]:
            return memo[n]
        res = fib_helper(n-1, memo) + fib_helper(n-2, memo)
        memo[n] = res
        return res
    return fib_helper(n, memo)

start = time()
print fib(33)
print time() - start

start = time()
print memo_fib(33)
print time() - start