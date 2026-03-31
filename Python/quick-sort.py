def quick_sort(arr):
    # Basisfall: Liste mit 0 oder 1 Element ist bereits sortiert
    if len(arr) <= 1:
        return arr
    
    # Pivot wählen (hier: erstes Element)
    pivot = arr[0]

    # Liste aufteilen
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Rekursiv sortieren und zusammenfügen
    return quick_sort(less) + equal + quick_sort(greater)


print(quick_sort([20, 3, 14, 1, 5]))
