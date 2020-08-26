
digits = "23"

if not digits:
    print []

phone = ('0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')

res = ['']
temp = []

for d in digits:
    for pre in res:
        for cur in phone[int(d)]:
            temp.append(pre+cur)

    res = temp
    temp = []

print res
