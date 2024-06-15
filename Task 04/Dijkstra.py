Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import heapq
>>> def dj(graph, start):
...     pq = [(0, start)]
...     distances = {node: float('inf') for node in graph}
...     distances[start] = 0
...     visited = set()
...     while pq:
...         currentDistance, currentNode = heapq.heappop(pq)
...         if currentNode in visited:
...             continue
...         visited.add(currentNode)
...         for neighbor, weight in graph[currentNode].items():
...             distance = currentDistance + weight
...             if distance < distances [neighbor]:
...                 distances[neighbor] = distance
...                 heapq.heappush(pq, (distance, neighbor))
...     return distances
... 
>>> graph = {
...     'A' : {'B': 1, 'C' : 4},
...     'B': {'C': 2, 'D': 5},
...     'C': {'D': 1},
...     'D': {}
...     }
>>> start = 'A'
>>> shortPath = dj(graph, start)
>>> 
>>> print(shortPath)
{'A': 0, 'B': 1, 'C': 3, 'D': 4}
