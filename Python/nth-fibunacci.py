def fibonacci(n):
    if n < 1:
        return 0
    
    if n < 3:
        return 1

    sequence = [0] * (n+1)
    sequence[1] = 1
    sequence[2] = 1

    for i in range(3, n+1):
        sequence[i] = sequence[i-1] + sequence[i-2]

    return sequence[n]


print(fibonacci(10))
