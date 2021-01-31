# This code gets TLE because of the large
# time complexity: O(n^2)

s = "eceba"

if len(s) < 3:
    print len(s)
    exit()

w_size = 0

for j in range(len(s)):

    box = {}
    point_store = []
    count = 0

    for i in range(j, len(s)):

        #  print s[i], box

        if not s[i] in box and count < 2:
            box[s[i]] = [i]
            count += 1

        elif s[i] in box and count < 3:
            box[s[i]].append(i)

        else:
            break

    for k, v in box.items():
        # print k, v
        for item in v:
            point_store.append(item)

        # print point_store
        w_size = max(w_size, (max(point_store) - min(point_store)) + 1)

print w_size