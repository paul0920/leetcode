import itertools

# Complexity: O(N) time, O(1) space

S = "(())()"

res = 0
l = 0

for a, b, in itertools.izip(S, S[1:]):

	print a, b, "l =", l, "res =", res

	if a + b == "()":
		res += 2 ** l

	if a == "(":
		l += 1

	else:
		l -= 1

	print a, b, "l =", l, "res =", res
	print ""

print res
