
S = "heeellooo"
words = ["hello", "hi", "helo"]

S = "abbbcd"
words = ["abbbbcd"]


s_size = len(S)
res = 0

for w in words:

    i_start, i_end = 0, 0
    j_start, j_end = 0, 0
    w_size = len(w)

    while i_start < s_size and j_start < w_size:

        if S[i_start] != w[j_start]:
            break

        while i_end < s_size and S[i_end] == S[i_start]:
            i_end += 1

        while j_end < w_size and w[j_end] == w[j_start]:
            j_end += 1

        if i_end - i_start != j_end - j_start and i_end - i_start < max(3, j_end - j_start):
            print S
            print w
            break

        i_start = i_end
        j_start = j_end

    if i_start == s_size and j_start == w_size:
        res += 1

print "count:", res
