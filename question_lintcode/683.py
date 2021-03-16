def wordBreak3(s, dict):
    # Write your code here
    max_length, lower_dict = init(dict)

    return memo_search(s.lower(), 0, lower_dict, max_length, {})


def memo_search(s, index, dict, max_length, memo):
    if index == len(s):
        return 1

    if index in memo:
        return memo[index]

    memo[index] = 0

    for i in range(index, len(s)):
        if i - index + 1 > max_length:
            break

        if s[index: i + 1] not in dict:
            continue

        memo[index] += memo_search(s, i + 1, dict, max_length, memo)
        # print index, i, memo[index]

    return memo[index]


def init(dict):
    max_length = 0
    lower_dict = set()

    for word in dict:
        max_length = max(max_length, len(word))
        lower_dict.add(word.lower())

    return max_length, lower_dict


s = "CatMat"
dict = ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
print wordBreak3(s, dict)
