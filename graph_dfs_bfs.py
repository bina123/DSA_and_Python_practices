from collections import deque
# Create this graph and test both traversals:

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Task 1: Write DFS function
def dfs_graph(graph, start, visited=None):
    """Graph DFS - visit all reachable nodes"""
    if visited is None:
        visited = set()
        
    visited.add(start)
    
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs_graph(graph,neighbour,visited)
            
    return visited

# Task 2: Write BFS function
def bfs_graph(graph, start):
    """Graph BFS - visit all reachable nodes"""
    visited = set()
    queue = deque([start])
    result = []
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
    return result

# Test both:
print("DFS from A:", dfs_graph(graph, 'A'))
print("BFS from A:", bfs_graph(graph, 'A'))
# Both should visit all 6 nodes