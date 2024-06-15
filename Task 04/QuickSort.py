Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def quickSort:
...     
SyntaxError: expected '('
>>> def quickSort(arr):
...     if len(arr) <= 1:
...         return arr
...     else:
...         pivot = arr[len(arr)//2]
...         left = [x for x in arr if x < pivot]
...         middle = [x for x in arr if x == pivot]
...         right = [x for x in arr if x > pivot]
...         return quickSort(left) + middle + quickSort(right)
... 
...     
>>> input = [3, 6, 8, 10, 1, 2, 1]
>>> sorted = quickSort(input)
>>> print(sorted)
[1, 1, 2, 3, 6, 8, 10]
