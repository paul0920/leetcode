
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

i = 0
j = len(height) - 1
area = 0

while i < j:

    area = max(area, (j - i) * min(height[i], height[j]))

    # This can either set to "<=" or "<"
    if height[i] < height[j]:
        i += 1

    else:
        j -= 1

print area
