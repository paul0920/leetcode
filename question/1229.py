
slots1 = [[216397070, 363167701], [98730764, 158208909], [441003187, 466254040], [558239978, 678368334],
          [683942980, 717766451]]
slots2 = [[50490609, 222653186], [512711631, 670791418], [730229023, 802410205], [812553104, 891266775],
          [230032010, 399152578]]
duration = 456085


i = 0
j = 0
slots1_sorted = sorted(slots1)
slots2_sorted = sorted(slots2)
curr_max_start = 0
curr_min_end = 0

while i < len(slots1) and j < len(slots2):

    start_1, end_1 = slots1_sorted[i]
    start_2, end_2 = slots2_sorted[j]
    curr_max_start = max(start_1, start_2)
    curr_min_end = min(end_1, end_2)

    if curr_min_end - curr_max_start >= duration:

        print [curr_max_start, curr_max_start + duration]
        exit()

    else:

        if end_1 > end_2:
            j += 1

        else:
            i += 1

print []
