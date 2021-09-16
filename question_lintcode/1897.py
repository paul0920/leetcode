def meetingRoomIII(intervals, rooms, ask):
    # Write your code here.
    if not rooms and ask:
        return [False] * len(ask)

    n = 50001
    time = [0] * n
    availability = [0] * n
    count = time[0]
    res = []

    for interval in intervals:
        start = interval[0]
        end = interval[1]
        time[start] += 1
        time[end] -= 1

    if count < rooms:
        availability[0] = 1

    for i in range(1, n):
        room_count = count + time[i]

        if room_count < rooms:
            availability[i] = availability[i - 1] + 1

        else:
            availability[i] = availability[i - 1]

        count = room_count

    for each_ask in ask:
        start = each_ask[0]
        end = each_ask[1]

        if availability[end - 1] - availability[start - 1] >= end - start:
            res.append(True)

        else:
            res.append(False)

    return res


Intervals = [[1, 2], [4, 5], [8, 10]]
rooms = 1
ask = [[2, 3], [3, 4]]
print meetingRoomIII(Intervals, rooms, ask)

