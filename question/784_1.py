
import itertools

S = "a1b2"

L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
print L

# "*L" make "L" into 4 parts
for i in itertools.product(*L):
    print i

print ""

# product treats "L" as one piece
for i in itertools.product(L, [0]):
    print i

print ""

print [''.join(i) for i in itertools.product(*L)]