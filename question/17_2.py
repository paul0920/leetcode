
digits = "23"

if not digits:
    print []

phone = ('0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')

res = ['']
for d in digits:

    res = [pre + cur for pre in res for cur in phone[int(d)]]

print res
