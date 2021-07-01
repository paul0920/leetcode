def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


a = 60
b = 48
print gcd(a, b)
