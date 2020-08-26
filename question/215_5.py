# Bucket sort algorithm
# Average time complexity: O(n)
#   Best case: O(n)
#   Worst case: O(n^2)
# Space complexity: O(nk), k: bucket count

# Bucket sort is mainly useful when input is uniformly distributed over a range
# Choose the bucket size & count, and put items in the corresponding bucket


nums = [3, 2, 1, 5, 6, 4]
# k = 2

# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4

# nums = [2, 200, 6, 9, 10, 32, 32, 100, 101, 123]

def bucket_sort(alist, bk_size):
    largest = max(alist)
    length = len(alist)
    size = bk_size

    # size = largest / length
    # if size < 1:
    #     size = 1
    print "bucket size:", size

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i] / size)

        print "i:", i, "j:", j, "length:", length
        if j < length:
            buckets[j].append(alist[i])

        elif j >= length:
            buckets[length - 1].append(alist[i])

        print buckets
        print ""

    # Use insertion sort to sort each bucket
    for i in range(length):
        insertion_sort(buckets[i])

    result = []
    for i in range(length):
        result += buckets[i]

    return result


def insertion_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1
        while j >= 0 and key < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = key


arr = bucket_sort(nums, 3)
print ""
print "the sorted array:", arr
