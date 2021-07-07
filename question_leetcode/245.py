def shortestWordDistance(wordsDict, word1, word2):
    """
    :type wordsDict: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    p1 = p2 = float("-INF")
    distance = len(wordsDict)

    for i, word in enumerate(wordsDict):
        if word == word1:
            distance = min(distance, i - p2)
            p1 = i

            if word1 == word2:
                p2 = i

        elif word == word2:
            distance = min(distance, i - p1)
            p2 = i

    return distance


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "makes"
print shortestWordDistance(wordsDict, word1, word2)
