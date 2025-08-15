print("Part 1 - get function name & arguments in wrapper")
"""
    Syntax:
    def decorator_name(func):
        def wrapper(*args, **kwargs):
            # Add functionality before the original function call
            result = func(*args, **kwargs)
            # Add functionality after the original function call
            return result
        return wrapper
    @decorator_name
    def function_to_decorate():
        # Original function code
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {str(func.__name__)}")
        print(f"*args received: {(str(args) if len(args) else "none")}")
        print(f"**kwargs received: {(str(kwargs) if len(kwargs) else "none")}")
        func()
        print(f"{str(func.__name__)} ended.")
    return wrapper

def decorator_with_keyword(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {str(func.__name__)}")
        print(f"*args received: {(str(args) if len(args) else "none")}")
        print(f"**kwargs received: {(str(kwargs) if len(kwargs) else "none")}")
        func(**kwargs)
        print(f"{str(func.__name__)} ended.")
    return wrapper

@decorator
def hello():
    print("Hello!")

@decorator_with_keyword
def say_hi_to(name):
    print(f"Say Hello to {name}!")

hello(["Alice", "Bob", "Cat"], tagging = "Testing")

say_hi_to("Randomness", name = "Democracy")

print('===' * 10)
print("Part 2 - Decorator Chaining with order")

def decor1(func): 
    def wrapper(): 
        print(f"Calling function {str(func.__name__)} by decor1.wrapper") 
        x = func()
        res = x * x
        print(res)
        return res
    return wrapper 

def decor2(func): 
    def wrapper():
        print(f"Calling function {str(func.__name__)} by decor2.wrapper")  
        x = func() 
        res = 2 * x 
        print(res)
        return res
    return wrapper 

@decor1
@decor2
def num(): 
    return 10

@decor2
@decor1
def num2():
    return 10
  
print("Finally:", num()) 
print('-' * 10)
print("Finally:", num2())