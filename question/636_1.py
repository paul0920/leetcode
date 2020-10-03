
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]


res = [0] * n
stack = []

for proc in logs:

    u_id, func_type, time = proc.split(":")
    u_id = int(u_id)
    time = int(time)

    if func_type == "start":

        if stack:
            res[stack[-1]] += time - pre_time

        stack += [u_id]
        # "pre_time" is the key since it stores the previous status!
        pre_time = time

    else:

        # time + 1 is the adjustment from end time to start time conversion
        res[stack.pop()] += time + 1 - pre_time
        pre_time = time + 1

print res
