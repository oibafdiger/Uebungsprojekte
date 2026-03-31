def square_root_bisection(number, tolerance=1e-6, maximum=100):
    # Handle negative input
    # Die Wurzel aus negativen Zahlen ist nicht reell
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    # Handle 0 and 1
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    # Wurzel muss zwischen der 0 und der Zahl selber sein
    low = 0
    high = max(1, number)

    # Set initial bounds
    for i in range(maximum):
        mid = (low + high) / 2

        # Check if within tolerance
        if abs(high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        
        # Adjust bounds
        # Wenn mid * mid zu kein -> Wurzel liegt rechts
        # Wenn mid * mid zu groß -> Wurzel liegt links
        # Interval wird halbiert
        if mid * mid < number:
            low = mid
        else:
            high = mid

    # If no cnvergence
    print(f"Failed to converge within {maximum} iterations")
    return None
        

print(square_root_bisection(0.001, 1e-7, 50))
