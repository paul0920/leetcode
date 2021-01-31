
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]


tank = gap = start = 0

for i in range(len(gas)):
    tank += gas[i]

    if tank >= cost[i]:
        tank -= cost[i]

    else:
        gap += cost[i] - tank
        start = i + 1
        tank = 0

    # print tank, gap

if start == len(gas) or tank < gap:
    print -1

print start
