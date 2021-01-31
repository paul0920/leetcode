
# Complexity: O(N) time, O(N) space

S = "(())()"

res = [0]

for i in S:
	if i == "(":
		res.append(0)

	else:
		close = res.pop()
		res[-1] += max(2 * close, 1)

print res[-1]
