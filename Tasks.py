Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fibonacci(n):
...     fib_sequence = []
...     a, b = 0, 1
...     for _ in range(n):
...         fib_sequence.append(a)
...         a, b = b, a + b
...     return fib_sequence
... 
>>> n = 5
>>> fib_series = fibonacci(n)
>>> print("Fibonacci series up to {n} terms: "fib_series)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("Fibonacci series up to {n} terms: ",fib_series)
Fibonacci series up to {n} terms:  [0, 1, 1, 2, 3]
>>> def is_palindrome(s):
...     cleaned = s.replace(" ", "").lower()
...     return cleaned == cleaned[::-1]
... 
>>> word = "racecar"
>>> result = is_palindrome(word)
>>> KeyboardInterrupt
>>> print(f"'{word}' is a palindrome: {result}")
'racecar' is a palindrome: True
