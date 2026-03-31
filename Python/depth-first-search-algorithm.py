def dfs(matrix, start):
    stack = [start]
    visited = set()
    result = []
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)

            # Nachbarn zur Matrix durchsuchen
            for neighbor in range(len(matrix[node])):
                if matrix[node] [neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
    
    return result
  


matrix = [
    [0, 1, 0, 0], 
    [1, 0, 1, 0], 
    [0, 1, 0, 1], 
    [0, 0, 1, 0]]

print(dfs(matrix, 1))
