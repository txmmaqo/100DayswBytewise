Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def lcs(X, Y):
...     m = len(X)
...     n = len(Y)
...     L = [[0] * (n + 1) for _ in range(m + 1)]
...     for i in range(m + 1):
...          for j in range(n + 1):
...              if i == 0 or j == 0:
...                  L[i][j] = 0
...              elif X[i-1] == Y[j-1]:
...                  L[i][j] = L[i-1][j-1] + 1
...              else:
...                  L[i][j] = max(L[i-1][j], L[i][j-1])
...     index = L[m][n]
...     lcs_str = [""] * (index + 1)
...     lcs_str[index] = ""
...     i = m
...     j = n
...     while i > 0 and j > 0:
...          if X[i-1] == Y[j-1]:
...             lcs_str[index-1] = X[i-1]
...             i -= 1
...             j -= 1
...             index -= 1
...          elif L[i-1][j] > L[i][j-1]:
...              i -= 1
...          else:
...              j -= 1
...     return "".join(lcs_str)
... 
>>> X = "AGGTAB"
>>> Y = "GXTXAYB"
>>> print(lcs(X, Y))
GTAB
