
intervals = [[0, 30], [5, 10], [15, 20]]

sch = []
count = 0
rm = 0

for i in intervals:
    for w in ((i[0], 1), (i[1], -1)):
        sch.append(w)

sch.sort()
print sch

for m, status in sch:
    count += status
    rm = max(rm, count)

print rm
