# Merge sort algorithm
# Average time complexity: O(n*logn)
#   Best case: O(n*logn)
#   Worst case: O(n*logn)
# Space complexity: O(n)

# Divide the array elements into 2 halves, compare and merge
# n elements and logn layers

# nums = [3, 2, 1, 5, 6, 4]
# k = 2

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4

# nums = [2, 200, 6, 9, 10, 32, 32, 100, 101, 123]

def merge_sort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr) / 2
		# Dividing the array elements into 2 halves
		L = arr[:mid]
		R = arr[mid:]
		print "Dividing...", L, R, "mid index:", mid
		merge_sort(L)
		merge_sort(R)

		i = j = k = 0

		print "Combining...", "L size:", len(L), ";", "R size:", len(R)

		# Copying data from sorted arrays L[] and R[] to the upper level
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1

			# The condition here is ">="
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			print "Left array,", "k:", k, "[", arr[k], "]"
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			print "Right array,", "k:", k, "[", arr[k], "]"
			j += 1
			k += 1

		print "Bottom and returning...", arr
		print ""


merge_sort(nums)
print nums
