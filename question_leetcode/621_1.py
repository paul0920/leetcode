import collections

tasks = ["A", "A", "A", "B", "B", "B"]
tasks = ["A", "B", "c", "D", "E", "A"]

n = 3


tasks_count = collections.Counter(tasks).values()
max_count = max(tasks_count)
max_count_freq = tasks_count.count(max_count)

print max(len(tasks), (max_count - 1) * (n + 1) + max_count_freq)
