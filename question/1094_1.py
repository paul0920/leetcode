
trips = [[3,2,7],[3,7,9],[8,3,9]]; capacity = 11

sch = []

for t in trips:
    for each in ((t[1], t[0]), (t[2], t[0] * -1)):
        sch.append(each)

sch.sort()

for time, status in sch:
    capacity -= status

    if capacity < 0:
        print False

print True
