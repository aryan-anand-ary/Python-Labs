# Lab 2: Unit I, Part 2 (Control Flow): Solutions

## Conditional Statements

<a id="q1"></a>
### Q1. Maximum of three numbers using nested if-else.
```python
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a >= b:
    if a >= c:
        print("Max =", a)
    else:
        print("Max =", c)
else:
    if b >= c:
        print("Max =", b)
    else:
        print("Max =", c)
```

<a id="q2"></a>
### Q2. Even or odd.
```python
n = int(input("Enter number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

<a id="q3"></a>
### Q3. Leap year.
```python
y = int(input("Enter year: "))
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```

<a id="q4"></a>
### Q4. Grade from marks using if-elif-else.
```python
m = float(input("Enter marks (0-100): "))
if m >= 90:
    print("Grade A+")
elif m >= 80:
    print("Grade A")
elif m >= 70:
    print("Grade B")
elif m >= 60:
    print("Grade C")
elif m >= 40:
    print("Grade D")
else:
    print("Fail")
```

<a id="q5"></a>
### Q5. Valid triangle from three angles.
```python
a = float(input("Angle 1: "))
b = float(input("Angle 2: "))
c = float(input("Angle 3: "))
if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("Valid triangle")
else:
    print("Not a valid triangle")
```

<a id="q6"></a>
### Q6. Profit or loss.
```python
cp = float(input("Cost price: "))
sp = float(input("Selling price: "))
if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No profit, no loss")
```

<a id="q7"></a>
### Q7. Divisible by both 3 and 6.
```python
n = int(input("Enter number: "))
if n % 3 == 0 and n % 6 == 0:
    print("Divisible by both 3 and 6")
else:
    print("Not divisible by both")
```

<a id="q8"></a>
### Q8. Temperature and humidity: check that values are provided.
```python
temp = input("Enter temperature: ").strip()
hum = input("Enter humidity: ").strip()
if temp == "" or hum == "":
    print("Values not provided")
else:
    print("Temperature:", temp, " Humidity:", hum)
```

<a id="q9"></a>
### Q9. In-hand salary (assumptions noted below).
```python
salary = float(input("Enter annual salary in lakh: "))

if salary <= 1:
    print('k')
else:
    hra = 0.10 * salary
    da = 0.05 * salary
    pf = 0.03 * salary

    if 5 <= salary <= 10:
        tax = 0.10 * salary
    elif 10 < salary <= 20:
        tax = 0.20 * salary
    elif salary > 20:
        tax = 0.30 * salary
    else:
        tax = 0        # 1-5 lakh: no slab given in the question

    in_hand = salary - (hra + da + pf + tax)
    print("In-hand salary (lakh) =", round(in_hand, 2))
```
*Assumptions: HRA, DA and PF are deducted as a percentage of salary, salaries between 1 and 5 lakh have no tax, and the 10-11 lakh gap is treated as the 10-20 lakh slab.*

## Loops

<a id="q10"></a>
### Q10. Sum of N natural numbers.
```python
n = int(input("N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)
```

<a id="q11"></a>
### Q11. Multiplication table.
```python
n = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

<a id="q12"></a>
### Q12. Reverse digits using while.
```python
n = int(input("Enter number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed =", rev)
```

<a id="q13"></a>
### Q13. Factorial using for.
```python
n = int(input("Enter number: "))
f = 1
for i in range(1, n + 1):
    f *= i
print("Factorial =", f)
```

<a id="q14"></a>
### Q14. Fibonacci up to n terms.
```python
n = int(input("Terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

<a id="q15"></a>
### Q15. Sum of digits.
```python
n = int(input("Enter number: "))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Sum of digits =", s)
```

<a id="q16"></a>
### Q16. Armstrong number.
```python
n = int(input("Enter number: "))
digits = len(str(n))
temp, total = n, 0
while temp > 0:
    total += (temp % 10) ** digits
    temp //= 10
print("Armstrong" if total == n else "Not Armstrong")
```

<a id="q17"></a>
### Q17. Narcissist number (4-digit).
```python
n = int(input("Enter a 4-digit number: "))
if 1000 <= n <= 9999:
    total = sum(int(d) ** 4 for d in str(n))
    print("Narcissist number" if total == n else "Not a narcissist number")
else:
    print("Not a 4-digit number")
```

## Nested Loops (Patterns)

Each program uses `N = 5`.

<a id="q18"></a>
### Q18. Right triangle
```python
N = 5
for i in range(1, N + 1):
    print("* " * i)
```

<a id="q19"></a>
### Q19. Inverted right triangle
```python
N = 5
for i in range(N, 0, -1):
    print("* " * i)
```

<a id="q20"></a>
### Q20. Number triangle
```python
N = 5
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

<a id="q21"></a>
### Q21. Repeated number triangle
```python
N = 5
for i in range(1, N + 1):
    for j in range(i):
        print(i, end=" ")
    print()
```

<a id="q22"></a>
### Q22. Alphabet triangle
```python
N = 5
for i in range(1, N + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
```

<a id="q23"></a>
### Q23. Floyd's triangle
```python
N = 5
num = 1
for i in range(1, N + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

<a id="q24"></a>
### Q24. Inverted number triangle
```python
N = 5
for i in range(N, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

<a id="q25"></a>
### Q25. Pyramid
```python
N = 5
for i in range(1, N + 1):
    print(" " * (N - i) + "*" * (2 * i - 1))
```

<a id="q26"></a>
### Q26. Inverted pyramid
```python
N = 5
for i in range(N, 0, -1):
    print(" " * (N - i) + "*" * (2 * i - 1))
```

<a id="q27"></a>
### Q27. Diamond
```python
N = 5
for i in range(1, N + 1):
    print(" " * (N - i) + "*" * (2 * i - 1))
for i in range(N - 1, 0, -1):
    print(" " * (N - i) + "*" * (2 * i - 1))
```

<a id="q28"></a>
### Q28. Palindrome number pyramid
```python
N = 5
for i in range(1, N + 1):
    print(" " * (N - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
```

<a id="q29"></a>
### Q29. Pascal's triangle
```python
N = 5
for i in range(N):
    print(" " * (N - i - 1), end="")
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()
```

## Control Structures

<a id="q30"></a>
### Q30. break, continue and pass.
```python
for i in range(1, 11):
    if i == 3:
        continue          # skip 3
    if i == 6:
        pass              # placeholder, does nothing
    if i == 8:
        break             # stop the loop at 8
    print(i, end=" ")
# Output: 1 2 4 5 6 7
```

<a id="q31"></a>
### Q31. Menu-driven conversion program.
```python
while True:
    print("\n1. cm to inches")
    print("2. km to miles")
    print("3. USD to INR")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        cm = float(input("cm: "))
        print("Inches =", cm / 2.54)
    elif choice == "2":
        km = float(input("km: "))
        print("Miles =", km * 0.621371)
    elif choice == "3":
        usd = float(input("USD: "))
        rate = float(input("Rate (INR per USD): "))
        print("INR =", usd * rate)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
```

## Command-Line Arguments

<a id="q32"></a>
### Q32. Sum of integer arguments using sys.argv.
```python
import sys
total = 0
for arg in sys.argv[1:]:
    total += int(arg)
print("Sum =", total)
# Run: python sum.py 10 20 30   ->   Sum = 60
```
