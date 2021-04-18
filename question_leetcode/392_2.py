def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if not s:
        return True

    n = len(s)
    m = len(t)
    s_pointer = 0
    t_pointer = 0

    if n > m:
        return False

    while s_pointer < n and t_pointer < m:
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1

        t_pointer += 1

    return True if s_pointer == n else False


s = "abc"
t = "ahbgdc"
print isSubsequence(s, t)
