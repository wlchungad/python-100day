def factorial(n):
    # Note: in mathematics, 0! = 1
    if n == 0: return 1
    if n == 1: return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n <= 0: return 0 
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

target = 10

print(f"{target}! = {factorial(target)}")
print(f"fibonacci({target}) = {fibonacci(target)}")
