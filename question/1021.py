
S = "(()())(())"

count = 0
c = ""

for p in S:

	if p == "(":
		count += 1

	if count > 1:
		c += p

	if p == ")":
		count -= 1

print c
