# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        kth = 1

        while reader.get(kth - 1) < target:
            kth *= 2

        left = 0
        right = kth

        while left + 1 < right:

            mid = left + (right - left) // 2

            if reader.get(mid) < target:
                left = mid

            else:
                right = mid

        if reader.get(left) == target:
            return left

        if reader.get(right) == target:
            return right

        return -1
