import collections
import bisect

rains = [1, 2, 0, 0, 2, 1]

box = collections.defaultdict(list)

# Index of days without rains
dry = []
status = []

for day, lake in enumerate(rains):

    if lake != 0:

        if len(box[lake]) >= 1:

            # Binary search time complexity: O(log n)
            idx_day_to_dry = bisect.bisect(dry, box[lake][-1])

            # No day to dry on this specific lake
            if idx_day_to_dry == len(dry):
                print []
                exit()

            status[dry[idx_day_to_dry]] = lake

            # Time complexity: O(n)
            dry.pop(idx_day_to_dry)

        box[lake].append(day)
        status.append(-1)

    else:
        dry.append(day)
        status.append(1)

print status
