
n = 7

square_list = []
num = 1
square_num = 1
q = set([n])
level = 0

while square_num <= n:
    square_list += [square_num]
    num += 1
    square_num = num ** 2

while q:

    level += 1
    next_q = set()

    for remainder in q:
        for square_n in square_list:

            if remainder == square_n:
                print level
                exit()

            elif remainder > square_n:
                next_q.add(remainder - square_n)

            else:
                break

    q = next_q
