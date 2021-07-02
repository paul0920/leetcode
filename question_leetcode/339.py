import collections


class NestedInteger(object):
    def __init__(self, _value=None, _list=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if _list is None:
            _list = []
        self.value = _value
        self.list = _list

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        if self.value is None:
            return False

        return True

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.value is not None:
            return self.value

        elif self.getList():
            return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.value is not None:
            return None

        return self.list


def depthSum(nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """
    if not nestedList:
        return 0

    queue = collections.deque(nestedList)
    res = 0
    depth = 1

    while queue:
        for _ in range(len(queue)):
            obj = queue.popleft()

            if obj.isInteger():
                res += obj.getInteger() * depth
                continue

            for item in obj.getList():
                queue.append(item)

        depth += 1

    return res


nestedList = [
    NestedInteger(None, [NestedInteger(1), NestedInteger(1)]),
    NestedInteger(2),
    NestedInteger(None, [NestedInteger(1), NestedInteger(1)])
]
print depthSum(nestedList)
