import functools

def call(func):

    @functools.wraps(func)

    def wrapper(*args, **kwargs):

        print("Calling function...")

        result = func(*args, **kwargs)

        print("Function executed.")

        return result
    
    return wrapper

@call
def square(num):
    return num * num

print(square(5))
