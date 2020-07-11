def gcd(a, b):  # a > b
    if b == 0 or a == 0:
        return a
    return gcd(b, a % b)

print(gcd(15, 12))
print(gcd(72, 27))