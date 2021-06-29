import collections

s = "cabwefgewcwaefgcf"
t = "cae"

s = "ADOBECODEBANC"
t = "ABC"

#s = "ab"
#t = "a"

s_item = len(s)
t_item = len(t)

if t_item > s_item or t_item == 0 or s == "":
    print ""
    exit()

# Count the characters in the t array
count_map = collections.Counter(t)

start, end = 0, s_item
i = 0

for j, c in enumerate(s):

    count_map[c] -= 1

    # This means c is in t
    if count_map[c] >= 0:
        t_item -= 1

    print j, s[j], i, s[i], count_map
    print j, i, j-i, " ", end, start, end-start

    # All chars in t were found
    if t_item == 0:

        # Start looking for the beginning index of the window
        while i < j and count_map[s[i]] < 0:

            print i, s[i]

            count_map[s[i]] += 1
            i += 1

        if j - i < end - start:
            start = i
            end = j

    print ""


# Doesn't find all chars. This means there is no matching window in s
if t_item:
    print ""
    exit()

print s[start: end + 1]
