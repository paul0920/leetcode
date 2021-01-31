
digits = "23"

if not digits:
    print []

phone = {"2": ["a", "b", "c"],
         "3": ["d", "e", "f"],
         "4": ["g", "h", "i"],
         "5": ["j", "k", "l"],
         "6": ["m", "n", "o"],
         "7": ["p", "q", "r", "s"],
         "8": ["t", "u", "v"],
         "9": ["w", "x", "y", "z"]}

res = []

if len(digits) == 1:
    print phone[digits]

def backtrack(res, letter, phone, digits, idx):

    if len(digits[idx:]) == 0:
        res.append(letter)
        return

    for n in phone[digits[idx]]:
        # print n, phone[digits[idx]]
        backtrack(res, letter + n, phone, digits, idx+1)


backtrack(res, "", phone, digits, 0)

print res
