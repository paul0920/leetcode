import itertools

text = "aaabaaa"

for a, b in itertools.groupby(text):
    # The returned group is itself an iterator that shares
    # the underlying iterable with groupby().
    # Because the source is shared,
    # when the groupby() object is advanced,
    # the previous group is no longer visible.
    # So, if that data is needed later,
    # it should be stored as a list:
    print a, b, list(b)
    print a, b, list(b)
    print ""


L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]

# Key function
key_func = lambda x: x[0]

for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))
    print(key + " :", list(group))
