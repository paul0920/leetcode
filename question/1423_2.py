
cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3

max_pts = sum(cardPoints[:k])
cal = max_pts

for i in range(1, k + 1):
    cal += -cardPoints[k - i] + cardPoints[-i]
    # print cal
    max_pts = max(max_pts, cal)

print max_pts
