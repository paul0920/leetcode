import collections
import heapq

n = 5
flights = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
src = 0
dst = 2
K = 2

g = collections.defaultdict(list)
current_price = [float('INF')] * n

for city_start, city_end, price in flights:
    g[city_start] += [(city_end, price)]
# [(price, # stop, start, path)]
q = [(0, -1, src, str(src))]

while q:

    price, total_stop, node, path = heapq.heappop(q)

    # Once we meet the destination node, heap sorting guarantees
    # the price is the global minimum
    if node == dst:
        print "[dst]:", node
        print "[final price]:", price, "[total stop]:", total_stop, "[prev path]:", path
        exit()

    for next_node, next_price in g[node]:

        update_price = price + next_price
        print path, "- - ->", next_node
        print "[est price]:", update_price, "[total stop]:", total_stop + 1, "[prev path]:", path

        if total_stop + 1 <= K:
        # if update_price <= current_price[next_node]:

        # By minimizing costs on all paths to every node and
        # limiting # of stop at the same time,
        # this only brings us a local minimum of the price.
        # Therefore, it's an incorrect implementation.
        # if update_price <= current_price[next_node] and total_stop + 1 <= K:

            current_price[next_node] = update_price
            heapq.heappush(q, (update_price, total_stop + 1, next_node, path + " -> " + str(next_node)))
            print q
            print ""

    print "[dst price]:", current_price[dst], " ", "[all prices]:", current_price
    print ""
    print ""

print current_price[dst] if current_price[dst] < float('INF') else -1
