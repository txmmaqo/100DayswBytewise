Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Breadth First:

from collections import deque
def bfs (graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order

graph = {0:[1, 2], 1:[2], 2:[0, 3], 3:[3]}
start_node = 2
print(bfs(graph, start_node))
[2, 0, 3, 1]
#Depth First
>>> def dfs(graph, start):
...     visited = set()
...     stack = [start]
...     dfs_order = []
...     while stack:
...         node = stack.pop()
...         if node not in visited:
...             visited.add(node)
...             dfs_order.append(node)
...             for neighbor in reversed(graph[node]):
...                 if neighbor not in visited:
...                     stack.append(neighbor)
...     return dfs_order
... 
>>> print (dfs(graph, start_node))
[2, 0, 1, 3]
