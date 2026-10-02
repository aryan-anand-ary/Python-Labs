# Lab 3: Unit II (Data Structures in Python): Solutions

## Strings

<a id="q1"></a>
### Q1. Count vowels and consonants.
```python
s = input("Enter string: ").lower()
v = c = 0
for ch in s:
    if ch.isalpha():
        if ch in "aeiou":
            v += 1
        else:
            c += 1
print("Vowels:", v, "Consonants:", c)
```

<a id="q2"></a>
### Q2. Reverse a string without slicing.
```python
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)
```

<a id="q3"></a>
### Q3. Palindrome string.
```python
s = input("Enter string: ").lower()
rev = ""
for ch in s:
    rev = ch + rev
print("Palindrome" if s == rev else "Not a palindrome")
```

<a id="q4"></a>
### Q4. Remove all punctuation.
```python
import string
s = input("Enter string: ")
result = "".join(ch for ch in s if ch not in string.punctuation)
print(result)
```

<a id="q5"></a>
### Q5. Character frequency using a dictionary.
```python
s = input("Enter string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
```

## Lists and Tuples

<a id="q6"></a>
### Q6. Sum of all elements.
```python
lst = [10, 20, 30, 40]
total = 0
for x in lst:
    total += x
print("Sum =", total)
```

<a id="q7"></a>
### Q7. Largest and smallest number.
```python
lst = [45, 12, 78, 3, 56]
print("Largest:", max(lst))
print("Smallest:", min(lst))
```

<a id="q8"></a>
### Q8. Remove duplicates from a list.
```python
lst = [1, 2, 2, 3, 4, 4, 5]
unique = []
for x in lst:
    if x not in unique:
        unique.append(x)
print(unique)      # order preserved
```

<a id="q9"></a>
### Q9. Sort a list of tuples by the second element.
```python
data = [(1, 5), (2, 3), (4, 1), (3, 4)]
data.sort(key=lambda t: t[1])
print(data)        # [(4, 1), (2, 3), (3, 4), (1, 5)]
```

<a id="q10"></a>
### Q10. Convert list to tuple and vice versa.
```python
lst = [1, 2, 3]
tpl = tuple(lst)
print(tpl, type(tpl))

back = list(tpl)
print(back, type(back))
```

## Dictionaries

<a id="q11"></a>
### Q11. Add, update and delete elements.
```python
d = {"name": "Neha", "age": 24}
d["city"] = "Lucknow"      # add
print(d)
d["age"] = 25              # update
print(d)
del d["city"]              # delete
print(d)
```

<a id="q12"></a>
### Q12. Merge two dictionaries.
```python
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = {**d1, **d2}      # or d1 | d2 (Python 3.9+)
print(merged)
```

<a id="q13"></a>
### Q13. Sort dictionary items by key and by value.
```python
d = {"b": 3, "a": 5, "c": 1}
by_key = dict(sorted(d.items()))
by_value = dict(sorted(d.items(), key=lambda item: item[1]))
print("By key  :", by_key)
print("By value:", by_value)
```

<a id="q14"></a>
### Q14. Convert lists of keys and values into a dictionary.
```python
keys = ["name", "age", "city"]
values = ["Neha", 24, "Lucknow"]
d = dict(zip(keys, values))
print(d)
```

<a id="q15"></a>
### Q15. Create an ordered dictionary.
```python
from collections import OrderedDict
od = OrderedDict()
od["one"] = 1
od["two"] = 2
od["three"] = 3
print(od)
od.move_to_end("one")      # OrderedDict-specific feature
print(od)
```

## Sets

<a id="q16"></a>
### Q16. Union, intersection and difference.
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A-B):", A - B)
```

<a id="q17"></a>
### Q17. Check whether two sets are disjoint.
```python
A = {1, 2, 3}
B = {4, 5, 6}
print("Disjoint" if A.isdisjoint(B) else "Not disjoint")
```

## Arrays

<a id="q18"></a>
### Q18. Array creation and operations using the array module.
```python
from array import array
arr = array('i', [10, 20, 30, 40])
arr.append(50)             # add at end
arr.insert(1, 15)          # insert at index
arr.remove(30)             # remove by value
print(arr)
print("Index of 40:", arr.index(40))
arr.reverse()
print("Reversed:", arr)
print("Popped:", arr.pop())
for x in arr:
    print(x, end=" ")
```

<a id="q19"></a>
### Q19. Matrix addition and multiplication using nested lists.
```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Addition
add = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
print("Addition:", add)

# Multiplication
mul = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            mul[i][j] += A[i][k] * B[k][j]
print("Multiplication:", mul)
```

<a id="q20"></a>
### Q20. Multi-dimensional arrays using numpy.
```python
import numpy as np      # pip install numpy
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Transpose:\n", a.T)
print("Sum of all:", a.sum())
print("Column sums:", a.sum(axis=0))

b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("Matrix product:\n", np.dot(a, b))
```
