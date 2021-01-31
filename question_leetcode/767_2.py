import collections

S = "aad"

if len(S) == 1:
    print S

count = collections.Counter(S)

# key (optional) - key function where the iterables are passed
# and comparison is performed based on its return value
digit0 = max(count.keys(), key=lambda x: count[x])

print count
print digit0

an = [digit0 for _ in range(count[digit0])]

print an

i = 0
for digit in count:
    if digit != digit0:
        for _ in range(count[digit]):
            an[i % len(an)] += digit
            print an, i
            i += 1

print "**********"
print ''.join(an) if i >= len(an) - 1 else ''
