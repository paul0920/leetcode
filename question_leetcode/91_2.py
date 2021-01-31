# len(input_num) = n
# Time complexity: O(n * 2^n)
# Space complexity: O(n)

input_num = "1000001"
input_num = "1121"
input_num = "1226"
curr_combination = ""
res = []


def decode_ways(i, curr_combination):

    if i == len(input_num):
        res.append(curr_combination)

        return

    num = int(input_num[i])
    if 1 <= num <= 9:
        curr_combination += chr(num - 1 + ord('A'))
        decode_ways(i + 1, curr_combination)
        curr_combination = curr_combination[:-1]

    if i + 1 < len(input_num):
        num = int(input_num[i]) * 10 + int(input_num[i + 1])
        if 10 <= num <= 26:
            curr_combination += chr(num - 1 + ord('A'))
            decode_ways(i + 2, curr_combination)


decode_ways(0, curr_combination)
print res
print len(res)
