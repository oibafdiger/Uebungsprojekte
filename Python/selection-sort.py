def selection_sort(arr):
    n = len(arr)
    
    # Gehe jede Position der Liste durch
    for i in range(n - 1):  # bis n-1, letzter ist automatisch korrekt
        min_index = i
        
        # Finde das kleinste Element im Rest der Liste
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Tausche nur, wenn das kleinste Element nicht schon an Position i ist
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

print(selection_sort([33, 1, 89, 2, 67, 245]))
