"""
    Now it is a generator function, it yields values
    This caused backtracking by calling sub-function impossible, as fibonacci(n-1) is a generator, not integer
    To achieve the same effect of 'return' version, we can use 'left and right' method (in this case, 'a' and 'b')
    This generator is much faster than functions and there will not be OOM
    We can call the result in a for loop as an enumerated list
"""
def fib(n):
    a, b = 0, 1
    for _ in range(n+1):
        yield a
        a, b = b, a + b

for i, val in enumerate(fib(100)):
    print (i, val)