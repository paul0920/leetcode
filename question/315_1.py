class Block(object):
    def __init__(self):
        self.total_count = 0
        self.bucket = {}


class Calculation(object):
    def __init__(self, size):
        self.block_list = [Block() for _ in range(size)]

    def count_smaller_num(self, num, block_size):
        block_index = num // block_size
        block_unit = self.block_list[block_index]
        count = 0

        for i in range(block_index):
            count += self.block_list[i].total_count

        for n in block_unit.bucket:
            if n < num:
                count += block_unit.bucket[n]

        return count

    def insert(self, num, block_size):
        block_index = num // block_size
        block_unit = self.block_list[block_index]
        block_unit.total_count += 1
        block_unit.bucket[num] = block_unit.bucket.get(num, 0) + 1


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        block_size = int((10 ** 4 * 2 + 1) ** 0.5) + 1
        calculation = Calculation(block_size)
        res = []

        for i in range(len(nums) - 1, -1, -1):
            # Need to offset all negative number to become positive numbers
            # in case of generating block_index < 0
            num_offset = nums[i] + 10 ** 4
            count = calculation.count_smaller_num(num_offset, block_size)
            # Use ".append(count)", O(1), instead of += [count], O(n)
            res.append(count)
            calculation.insert(num_offset, block_size)

        return res[::-1]


nums = [5, 2, 6, 1]
obj = Solution()
print obj.countSmaller(nums)
