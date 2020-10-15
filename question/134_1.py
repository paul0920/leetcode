
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]


if not len(gas) or not len(cost) or sum(gas) < sum(cost):
    print -1

start = 0
cur_gas = 0
min_gas_remaining = float('INF')

for i in range(len(gas)):
    cur_gas += gas[i] - cost[i]

    if cur_gas < min_gas_remaining:
        min_gas_remaining = cur_gas
        start = (i + 1) % len(gas)

print start
