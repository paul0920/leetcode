import collections

# text = "ababa"
# text = "aaabaaa"
# text = "aaaaaab"
text = "aaabbaaa"

mx = 1
ct = collections.Counter(text)
l = len(text)
st = i = 0

while i < l:

	if text[i] != text[st]:
		j = i + 1

		# Find the same char of next group
		while j < l and text[j] == text[st]:
			j += 1

		count = (j - 1) - st

		print "i:", i, "st:", st, "j:", j, "count:", count

		# It has one extra char to swap
		if count < ct[text[st]]:
			count += 1

		print "mx:", mx, "count:", count
		print ""

		mx = max(mx, count)
		st = i

	i += 1

# Process the last group
count = i - st
print "i:", i, "st:", st, "count:", count

if count < ct[text[st]]:
	count += 1

print "mx:", mx, "count:", count
print ""

mx = max(mx, count)

print mx
