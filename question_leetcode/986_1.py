# A = [[3,5],[9,20]]
# B = [[4,5],[7,10],[11,12],[14,15],[16,20]]

A = [[0, 4], [7, 8], [8, 10]]
B = [[0, 7], [14, 15], [18, 20]]

window = A + B
window.sort()
res = []
idx = 0
offset = 0

print window

# Need to enhance the code further to detect whether
# there is any overlap intervals among A and B list themselves
# such as [7, 8] and [8, 10]
while idx < len(window) - 1:

    print window[idx + offset], window[idx + 1]

    if window[idx + offset][1] >= window[idx + 1][0]:

        if window[idx + 1][1] < window[idx + offset][1]:
            res.append([window[idx + 1][0], window[idx + 1][1]])
            offset -= 1

        else:
            res.append([window[idx + 1][0], window[idx + offset][1]])
            offset = 0

    else:
        offset = 0

    idx += 1

print res
