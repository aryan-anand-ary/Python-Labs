# Lab 4: Unit III (Functions, Modules, Regular Expressions): Solutions

## Functions

**Q1. Factorial.**
```python
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

print(factorial(5))     # 120
```

**Q2. Prime check.**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))     # True
```

**Q3. List: return sum and average.**
```python
def sum_avg(lst):
    total = sum(lst)
    return total, total / len(lst)

s, a = sum_avg([10, 20, 30, 40])
print("Sum =", s, "Average =", a)
```

**Q4. Rectangle area with default arguments.**
```python
def rect_area(length=5, breadth=3):
    return length * breadth

print(rect_area())          # 15 (defaults)
print(rect_area(10, 4))     # 40
print(rect_area(breadth=2)) # 10
```

## Variable-Length Arguments

**Q5. Demonstrate variable-length arguments.**
```python
def show(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

show(1, 2, 3, name="Neha", city="Lucknow")
```

**Q6. second_largest(*args) without set().**
```python
def second_largest(*args):
    unique = []
    for x in args:
        if x not in unique:
            unique.append(x)
    if len(unique) < 2:
        return None
    first = second = float("-inf")
    for x in unique:
        if x > first:
            second = first
            first = x
        elif x > second:
            second = x
    return second

print(second_largest(10, 40, 40, 30, 20))   # 30
```

**Q7. analyze_numbers(*args).**
```python
def analyze_numbers(*args):
    evens = [x for x in args if x % 2 == 0]
    odds = [x for x in args if x % 2 != 0]
    print("Even numbers:", evens)
    print("Odd numbers:", odds)
    print("Sum of evens:", sum(evens))
    print("Sum of odds:", sum(odds))
    print("Count of evens:", len(evens))
    print("Count of odds:", len(odds))

analyze_numbers(1, 2, 3, 4, 5, 6, 7)
```

**Q8. student_result(**kwargs).**
```python
def student_result(**kwargs):
    total = sum(kwargs.values())
    percentage = total / len(kwargs)          # each subject out of 100
    top = max(kwargs, key=kwargs.get)
    passed = all(m >= 40 for m in kwargs.values())
    print("Total marks:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Highest scoring subject:", top, "(", kwargs[top], ")")
    print("Result:", "Pass" if passed else "Fail")

student_result(Maths=78, Physics=65, Chemistry=39, English=82)
```

**Q9. employee_salary(*args, **kwargs).**
```python
def employee_salary(*args, **kwargs):
    # args = salaries, kwargs = name=salary
    avg = sum(args) / len(args)
    print("Average salary:", avg)
    print("Highest salary:", max(args))
    print("Lowest salary:", min(args))
    print("Employees above average:")
    for name, sal in kwargs.items():
        if sal > avg:
            print("  ", name, sal)

employee_salary(30000, 45000, 60000, 25000,
                Amit=30000, Neha=45000, Rahul=60000, Priya=25000)
```

**Q10. generate_bill(*args, **kwargs).**
```python
def generate_bill(*args, **kwargs):
    # args = item prices, kwargs = item=quantity (same order as prices)
    quantities = list(kwargs.values())
    total = sum(p * q for p, q in zip(args, quantities))
    total_qty = sum(quantities)
    avg_price = sum(args) / len(args)

    print("Total bill:", total)
    print("Total quantity:", total_qty)
    print("Average price:", round(avg_price, 2))

    if total > 5000:
        discount = total * 0.10
        print("Discount (10%):", discount)
        total -= discount
    print("Final payable amount:", total)

generate_bill(1200, 800, 500, Laptop_bag=2, Mouse=3, Pen_drive=4)
```

## Lambda, map, filter, reduce

**Q11. Lambda for square and cube.**
```python
square = lambda x: x ** 2
cube = lambda x: x ** 3
print(square(4), cube(3))      # 16 27
```

**Q12. map(), filter(), reduce().**
```python
from functools import reduce
nums = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x ** 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
total = reduce(lambda a, b: a + b, nums)

print("Squares:", squares)
print("Evens:", evens)
print("Sum:", total)
```

## Decorators and Generators

**Q13. Decorator that adds logging before a function call.**
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

print(add(3, 4))
```

**Q14. Generator function for Fibonacci.**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for x in fibonacci(10):
    print(x, end=" ")
```

## Standard Library Modules

**Q15. math module: trigonometric and logarithmic values.**
```python
import math
angle = math.radians(30)
print("sin(30):", round(math.sin(angle), 4))
print("cos(30):", round(math.cos(angle), 4))
print("tan(30):", round(math.tan(angle), 4))
print("log(100) natural:", math.log(100))
print("log10(100):", math.log10(100))
print("log2(8):", math.log2(8))
```

**Q16. Random password generator.**
```python
import random
import string

length = int(input("Password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))
print("Generated password:", password)
```
*For real security, use the `secrets` module instead of `random`.*

**Q17. System information using os and sys.**
```python
import os
import sys
import platform

print("OS name:", os.name)
print("Platform:", platform.system(), platform.release())
print("Current directory:", os.getcwd())
print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("CPU count:", os.cpu_count())
print("Files here:", os.listdir("."))
```

## Custom Modules

**Q18. Own module for arithmetic operations.**

`arith.py`
```python
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Division by zero"
```
`main.py`
```python
import arith
print(arith.add(10, 5), arith.sub(10, 5), arith.mul(10, 5), arith.div(10, 5))
```

**Q19. second_largest.py: third largest unique number without set().**

`second_largest.py`
```python
def get_numbers():
    return list(map(int, input("Enter integers separated by space: ").split()))

def third_largest(numbers):
    unique = []
    for x in numbers:
        if x not in unique:
            unique.append(x)
    if len(unique) < 3:
        return None
    first = second = third = float("-inf")
    for x in unique:
        if x > first:
            first, second, third = x, first, second
        elif x > second:
            second, third = x, second
        elif x > third:
            third = x
    return third
```
`main.py`
```python
import second_largest as sl

nums = sl.get_numbers()
result = sl.third_largest(nums)
if result is None:
    print("Fewer than 3 unique numbers")
else:
    print("Third largest unique number:", result)
```

**Q20. analyze_number.py**

`analyze_number.py`
```python
def get_numbers():
    return list(map(int, input("Enter integers separated by space: ").split()))

def analyze(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    odds = [x for x in numbers if x % 2 != 0]
    return {
        "evens": evens,
        "odds": odds,
        "sum_even": sum(evens),
        "sum_odd": sum(odds),
        "count_even": len(evens),
        "count_odd": len(odds),
        "avg_even": sum(evens) / len(evens) if evens else 0,
        "avg_odd": sum(odds) / len(odds) if odds else 0,
    }
```
`main.py`
```python
import analyze_number as an

r = an.analyze(an.get_numbers())
print("Even numbers:", r["evens"])
print("Odd numbers:", r["odds"])
print("Sum of even:", r["sum_even"])
print("Sum of odd:", r["sum_odd"])
print("Count of even:", r["count_even"])
print("Count of odd:", r["count_odd"])
print("Average of even:", r["avg_even"])
print("Average of odd:", r["avg_odd"])
```

**Q21. student_result.py**

`student_result.py`
```python
def get_marks():
    n = int(input("Number of subjects: "))
    marks = {}
    for _ in range(n):
        name = input("Subject name: ")
        marks[name] = float(input("Marks: "))
    return marks

def calculate(marks):
    total = sum(marks.values())
    percentage = total / (len(marks) * 100) * 100
    top = max(marks, key=marks.get)
    passed = all(m >= 40 for m in marks.values())
    return total, percentage, top, passed
```
`main.py`
```python
import student_result as sr

marks = sr.get_marks()
total, pct, top, passed = sr.calculate(marks)
print("Total marks:", total)
print("Percentage:", round(pct, 2), "%")
print("Highest scoring subject:", top)
print("Result:", "Pass" if passed else "Fail")
```

**Q22. employee_salary.py**

`employee_salary.py`
```python
def get_employees():
    n = int(input("Number of employees: "))
    emp = {}
    for _ in range(n):
        name = input("Name: ")
        emp[name] = float(input("Salary: "))
    return emp

def analyze(emp):
    sal = list(emp.values())
    avg = sum(sal) / len(sal)
    high, low = max(sal), min(sal)
    return {
        "avg": avg,
        "high": high,
        "low": low,
        "high_names": [n for n, s in emp.items() if s == high],
        "low_names": [n for n, s in emp.items() if s == low],
        "above_avg": [n for n, s in emp.items() if s > avg],
    }
```
`main.py`
```python
import employee_salary as es

r = es.analyze(es.get_employees())
print("Average salary:", r["avg"])
print("Highest salary:", r["high"])
print("Lowest salary:", r["low"])
print("Highest earners:", r["high_names"])
print("Lowest earners:", r["low_names"])
print("Above average:", r["above_avg"])
```

**Q23. circle_area.py**

`circle_area.py`
```python
import math

def get_radius():
    return float(input("Enter radius: "))

def area(r):
    return math.pi * r ** 2

def circumference(r):
    return 2 * math.pi * r
```
`main.py`
```python
import circle_area as ca

r = ca.get_radius()
print("Area:", round(ca.area(r), 2))
print("Circumference:", round(ca.circumference(r), 2))
```

**Q24. rectangle_area.py**

`rectangle_area.py`
```python
def get_dimensions():
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    return l, b

def perimeter(l, b):
    return 2 * (l + b)
```
`main.py`
```python
import rectangle_area as ra

l, b = ra.get_dimensions()
print("Perimeter:", ra.perimeter(l, b))
```

## Regular Expressions

**Q25. Validate an email address.**
```python
import re
email = input("Enter email: ")
pattern = r"^[\w.+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"
print("Valid email" if re.match(pattern, email) else "Invalid email")
```

**Q26. Extract all numbers from text.**
```python
import re
text = "I have 3 apples, 12 oranges and 4.5 kg of grapes."
print(re.findall(r"\d+\.?\d*", text))    # ['3', '12', '4.5']
```

**Q27. Replace all whitespace with a single space.**
```python
import re
s = "Python    is   \t  fun\nand   easy"
print(re.sub(r"\s+", " ", s))
```

**Q28. Words starting with a capital letter.**
```python
import re
text = "Neha and Rahul live in Lucknow near the Gomti river."
print(re.findall(r"\b[A-Z][a-zA-Z]*\b", text))
```

**Q29. Validate phone numbers (10-digit Indian mobile, optional +91).**
```python
import re
phone = input("Enter phone number: ")
pattern = r"^(\+91[\-\s]?)?[6-9]\d{9}$"
print("Valid phone number" if re.match(pattern, phone) else "Invalid phone number")
```
