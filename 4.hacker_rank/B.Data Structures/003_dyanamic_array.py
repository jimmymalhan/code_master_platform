def dynamicArray(n, queries):
    sequences = [[] for x in range(n)]
    answer = []
    lastAnswer = 0
    for query in queries:
        action, i, v = list(map(int, query))
        idx = (i^lastAnswer)%n
        if action == 1:
            sequences[idx].append(v)
        else:
            temp = sequences[idx]
            lastAnswer = sequences[idx][v%len(temp)]
            answer.append(lastAnswer)
    return answer
