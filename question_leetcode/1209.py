
#s = "deeedbbcccbdaa"; k = 3
#s = "beeebba"; k = 3
s = "ees"; k = 3

s1 = list(s)
n = len(s1)

while n >= k:
	repeatcnt = 1
	offset = 0

	# Process k adjacent duplicates in current status
	for i in range(1, n):
		slow = i - offset
		print "slow =", slow, "	", "i =", i, "	", "offset =", offset
		print "s1[i] =", s1[i], "	", "s1 =", s1
		print ""

		if slow > 0 and s1[i] == s1[slow - 1]:
			repeatcnt += 1
			if repeatcnt == k:
				offset += k
				repeatcnt = 1
				continue

		else:
			repeatcnt = 1

		# Build the next phase of the array after removing
		# k adjacent duplicates
		s1[slow] = s1[i]

	print "offset =", offset
	if not offset:
		break

	# Reduce the array size to the next status
	n -= offset
	print s1, n

print ''.join(s1[:n])
