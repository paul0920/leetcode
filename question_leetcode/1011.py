
weights = [3,2,2,4,1,4]
D = 3

left, right = max(weights), sum(weights)

while left <= right:

	mid = (left + right) / 2
	estD = 1
	curr_load = 0

	print "L:", left, "Mid:", mid, "R:", right

	# This is the core part of the search!
	for w in weights:

		if curr_load + w > mid:
			estD += 1
			curr_load = 0

		curr_load += w

		print "estD:", estD, "curr_load:", curr_load

	if estD > D:
		left = mid + 1

	else:
		right = mid - 1

	print "L:", left, "old_Mid:", mid, "R:", right
	print ""

# Return "left" instead of "right" because it's the minimum
# weight capacity of the ship
print left
