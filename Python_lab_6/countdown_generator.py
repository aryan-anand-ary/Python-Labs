import functools

def countdown(n):
    while n >= 1:
        yield n
        n -= 1

for x in countdown(5):
    print(x)   