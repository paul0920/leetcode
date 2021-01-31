# Brute force solution
# Time complexity: O(n^2)
# Space complexity: O(1) extra space

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = 0

# Search starting from the left 2nd to the right 2nd items
for i in range(1, len(height) - 1):

    max_left = max(height[:i])
    max_right = max(height[i + 1:])
    potential = min(max_left, max_right) - height[i]
    ans += max(0, potential)

    print i, max_left, max_right, height[i], "", potential

print ans