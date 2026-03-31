def dfs_n_queens(n):
    if n < 1:
        return []
    
    results = []
    
    def is_valid(current, col):
        row = len(current)
        
        for r in range(row):
            c = current[r]
            
            # gleiche Spalte
            if c == col:
                return False
            
            # gleiche Diagonale
            if abs(c - col) == abs(r - row):
                return False
        
        return True
    
    def dfs(row, current):
        # alle Damen platziert
        if row == n:
            results.append(current[:])
            return
        
        # versuche jede Spalte
        for col in range(n):
            if is_valid(current, col):
                current.append(col)     # setze Dame
                dfs(row + 1, current)   # gehe tiefer
                current.pop()           # backtracking
    
    dfs(0, [])
    return results
