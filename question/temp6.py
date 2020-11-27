def answer(maze):
    if len(maze) < 2 or len(maze) > 20 or len(maze[0]) < 2 or len(maze[0]) > 20:
        return 0
    map_start = bfs(maze, [0, 0])
    # print map_start
    map_end = bfs(maze, [len(maze) - 1, len(maze[0]) - 1])
    ones = getOnes(maze)

    #   print map_start
    #   print map_end
    #   print ones

    min = 1000 * 1000 * 1000
    for one in ones:
        print "one:", one
        adj1 = getAdj(one, map_start)
        adj2 = getAdj(one, map_end)
        print "1:", adj1
        print "2:", adj2
        if not adj1 or not adj2:
            continue
        sum = adj1 + adj2 + 1
        print sum
        print ""
        if sum < min:
            min = sum

    # x = map_start[nodeToString([len(maze)-1, len(maze[0])-1])] if nodeToString([len(maze)-1, len(maze[0])-1]) in map_start else 0
    return min


def getAdj(one, map):
    l = []
    node = stringtoNode(one)
    x = node[0]
    y = node[1]
    a = nodeToString([x + 1, y])
    b = nodeToString([x - 1, y])
    c = nodeToString([x, y + 1])
    d = nodeToString([x, y - 1])

    if a in map:
        l.append(map[a])
    if b in map:
        l.append(map[b])
    if c in map:
        l.append(map[c])
    if d in map:
        l.append(map[d])
    print l
    if len(l) == 0:
        return None
    else:
        return min(l)


def getOnes(maze):
    l = []
    for x in range(0, len(maze)):
        for y in range(0, len(maze[0])):
            #   print x
            #   print y
            if maze[x][y] == 1:
                l.append(nodeToString([x, y]))

    # print l
    return l


def bfs(maze, first):
    queue = []
    dict = {}
    queue.append(first)
    dict[nodeToString(first)] = 1

    while len(queue) > 0:

        current = queue.pop(0)
        # print current

        # add valid nodes to queue
        for neighbor in getNeighbors(current, maze):
            if neighbor[0] < 0 or neighbor[0] > len(maze) - 1 or neighbor[1] < 0 or neighbor[1] > len(maze[0]) - 1:
                pass
            else:
                if maze[neighbor[0]][neighbor[1]] == 0 and nodeToString(neighbor) not in dict:
                    queue.append(neighbor)
                    dict[nodeToString(neighbor)] = dict[nodeToString(current)] + 1
                else:
                    pass
    return dict


def stringtoNode(s):
    # print s, "hi"
    a = s.split('-')
    return [int(a[0]), int(a[1])]


def nodeToString(node):
    test = str(node[0]) + '-' + str(node[1])
    return test


def getNeighbors(current, maze):
    x = current[0]
    y = current[1]
    neighbors = []

    neighbors.append([x + 1, y])
    neighbors.append([x, y + 1])
    neighbors.append([x - 1, y])
    neighbors.append([x, y - 1])

    return neighbors


# maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [0,0,0,1], [0,1,1,1], [0,0,0,0]]
# maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]]
print answer(maze)

# def answer(maze):
#     # your code here
#   if len(maze) < 2 or len(maze) > 20 or len(maze[0]) < 2 or len(maze[0]) > 20:
#     return 0
#   path = []
#   return recurse(maze, 0, 0, path)


# def recurse(maze, x, y, path):

#   if x < 0 or x > len(maze)-1 or y < 0 or y > len(maze[0])-1:
#     return False
#   if maze[x][y] == 1:
#     return False

#   if x == len(maze)-1 and y == len(maze[0])-1:
#     if maze[x][y] == 0:
#       path.append([x,y])
#       return True
#     else:
#       return False


#   maze[x][y] = 1
#   path.append([x, y])

#   ans = recurse(maze, x+1, y, path) or recurse(maze, x, y+1, path) or recurse(maze, x-1, y, path) or recurse(maze, x, y-1, path)

#   if ans:
#     return len(path)

#   maze[x][y] = 0
#   path.pop()

#   return 0


# # maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [0,0,0,1], [0,1,1,1], [0,0,0,0]]
# # maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# print answer(maze)


# def answer(maze):

#   height = len(maze)
#   width = len(maze[0])

#   if width < 2 or width > 20 or height < 2 or height > 20:
#     return 0

#   if maze[0][0] != 0 or maze[height-1][width-1] != 0:
#     return 0

#   # return 'hello'
#   return recurse(maze, height, width, 0, 0, 1)


# def recurse(maze, height, width, y, x, steps):

#   if y < 0 or y > height-1 or x < 0 or x > width-1:
#     return 0
#   if maze[y][x] == 1:
#     return 0

#   maze[x][y] = 1

#   if y == height-1 and x == width-1:
#     return steps


#   steps = 0

#   return recurse(maze, height, width, x+1, y, steps+1) + recurse(maze, height, width, x, y+1, steps+1)


# maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]

# print answer(maze)