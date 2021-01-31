
target = [1, 3]

def build():
    curr = 1
    for num in target:
        yield 'Push'
        while curr < num:
            yield 'Pop'
            yield 'Push'
            curr += 1
        curr += 1


print list(build())
