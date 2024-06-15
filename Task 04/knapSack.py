Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def knapSack(weights, values, capacity):
...     n = len(weights)
...     dp = [[0 for _ in range (capacity + 1)] for _ in range (n+1)]
...     for i in range (1, n+1):
...         for w in range (1, capacity + 1):
...             if weights [i-1] <= w:
...                 dp [i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
...             else:
...                 dp[i][w] = dp[i-1][w]
...     return dp[n][capacity]
... 
>>> weights = [1,3,4,5]
>>> values = [1, 4, 5, 7]
>>> capacity = 7
>>> maxValue = knapSack(weights, values, capacity)
>>> print(maxValue)
9
