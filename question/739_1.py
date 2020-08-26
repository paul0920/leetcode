
T = [73, 74, 75, 71, 69, 72, 76, 73]

res = []

for i in range(len(T)):
    for j in range(i, len(T)):

        if i != j and T[i] < T[j]:
            res.append(j - i)
            break

        elif j == len(T) - 1:
            res.append(0)

        # print res, i, j

print res
