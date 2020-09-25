from heapq import heappush, heappop
from collections import Counter

tasks = ["A", "A", "A", "B", "B", "B"]
tasks = ["A", "B", "c", "D", "E", "A"]
tasks = ["A", "A", "A", "A", "B", "B", "D", "E"]

n = 2


task_count = Counter(tasks)
current_time = 0
current_heap = []

for k, v in task_count.items():
    heappush(current_heap, (v * -1, k))

while current_heap:

    index, temp = 0, []

    while index <= n:

        current_time += 1

        if current_heap:

            timing, task_id = heappop(current_heap)
            if timing != -1:
                temp.append((timing + 1, task_id))

        if not current_heap and not temp:
            break

        else:
            index += 1

    for item in temp:
        heappush(current_heap, item)

print current_time
