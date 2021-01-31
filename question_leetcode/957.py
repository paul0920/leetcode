
cells = [0, 1, 0, 1, 1, 0, 0, 1]
N = 100

next_cells = cells[::]
seen = {}
# Assigning this at the beginning can reduce one cycle
# of the repeated pattern
# seen = {str(next_cells): N}

while N:

    temp_cells = next_cells[:]

    for i in range(1, len(next_cells) - 1):
        next_cells[i] = temp_cells[i - 1] ^ temp_cells[i + 1] ^ 1

        # if (temp_cells[i - 1] == temp_cells[i + 1] == 0) or (temp_cells[i - 1] == temp_cells[i + 1] == 1):
        #     next_cells[i] = 1
        #
        # else:
        #     next_cells[i] = 0

    next_cells[0] = 0
    next_cells[-1] = 0
    N -= 1

    # Found the repeated pattern and fast-forward to reduce the time complexity
    if str(next_cells) in seen:
        N %= (seen[str(next_cells)] - N)

    seen[str(next_cells)] = N

print next_cells
