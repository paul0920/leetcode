
cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3

w_size = len(cardPoints) - k
cardPoints = [0] + cardPoints
total_pts = sum(cardPoints)
max_pts = 0

for i in range(1, len(cardPoints)):

    cardPoints[i] += cardPoints[i - 1]
    # print cardPoints, total_pts

    if i >= w_size:
        max_pts = max(max_pts, total_pts - cardPoints[i] + cardPoints[i - w_size])

print max_pts
