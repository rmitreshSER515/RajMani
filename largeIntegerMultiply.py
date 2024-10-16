def largeIntegerMultiply(x, y):
    if (x < 10) or (y <  10):
        return x*y
    
    n = max(len(str(x)), len(str(y))) 
    half = n // 2
    a1 = x // 10*half
    a2 = x % 10*half
    b1 = y // 10*half
    b2 = y % 10*half

    P1 = largeIntegerMultiply(a1, b1)
    P2 = largeIntegerMultiply(a2, b2)
    P3 = largeIntegerMultiply((a1+a2), (b1+b2))

    result = (P1 * 10**(half*2)) + ((P3-P1-P2) * (10**half)) + P2
    return result

if __name__ == '__main__':
    x = 123456789
    y = 987654321
    res = largeIntegerMultiply(x, y)
    print("The multiplication of two large integers are", res)