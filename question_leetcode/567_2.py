def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if not s1:
        return True

    if s1 and not s2:
        return False

    s1_counts = {}
    s2_counts = {}
    left = 0
    right = len(s1)

    for c in s1:
        s1_counts[c] = s1_counts.get(c, 0) + 1

    for c in s2[:len(s1)]:
        s2_counts[c] = s2_counts.get(c, 0) + 1

    while right < len(s2):
        if s1_counts == s2_counts:
            return True

        left_char = s2[left]
        right_char = s2[right]
        s2_counts[left_char] -= 1
        s2_counts[right_char] = s2_counts.get(right_char, 0) + 1

        # Use .pop() to remove item from hash table
        if s2_counts[left_char] <= 0:
            s2_counts.pop(left_char)

        left += 1
        right += 1

    return s1_counts == s2_counts


s1 = "ab"
s2 = "eidbaooo"
s1 = "dinitrophenylhydrazine"
s2 = "acetylphenylhydrazine"
print checkInclusion(s1, s2)
