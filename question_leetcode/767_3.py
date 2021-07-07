import collections
import heapq


def reorganizeString(s):
    """
    :type s: str
    :rtype: str
    """
    char_to_count = collections.Counter(s)
    heap = []
    string = ""
    prev_largest_count = 0

    for char, count in char_to_count.items():
        heapq.heappush(heap, (-count, char))

    while heap:
        largest_count, char = heapq.heappop(heap)
        string += char

        if prev_largest_count < 0:
            heapq.heappush(heap, (prev_largest_count, prev_char))

        prev_largest_count = largest_count + 1  # hold this char and insert it next round
        prev_char = char

    return string if len(string) == len(s) else ""


s = "aab"
print reorganizeString(s)
