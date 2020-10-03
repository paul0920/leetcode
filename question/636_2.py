
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]


res = [0] * n
stack = []

for proc in logs:

    u_id, func_type, time = proc.split(":")
    u_id = int(u_id)
    time = int(time)

    if func_type == "start":
        stack.append(time)

    else:
        delta = time + 1 - stack.pop()
        res[u_id] += delta

        stack = [t + delta for t in stack]

print res
