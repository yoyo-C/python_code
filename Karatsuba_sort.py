def karatsuba(num1, num2):
    num1Str = str(num1)
    num2Str = str(num2)
    if (num1 < 10) or (num2 < 10):
        return num1 * num2
    maxLength = max(len(num1Str), len(num2Str))
    splitPosition = maxLength / 2

    high1, low1 = int(num1Str[:-splitPosition]), int(num1Str[-splitPosition:])
    high2, low2 = int(num2Str[:-splitPosition]), int(num2Str[-splitPosition:])

    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high2, high1)

    return (z2 * 10 **(2 * splitPosition)) + z0 + (z1 - z0 - z2) * 10 **(splitPosition)

print karatsuba(222222, 3333)