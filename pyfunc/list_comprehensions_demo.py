arr = [1, 2, 3]
box = []

for a in arr:
    for b in arr:
        box.append(a + b)

print box
print [a + b for a in arr for b in arr]




# If & Else
print [n if n % 2 else 'N' for n in range(10)]
# print [n for n in range(10) if n % 2 else 'N'] # Wrong usage

# If
print [n for n in range(10) if n % 2]
# print [n if n % 2 for n in range(10)] # Wrong usage
