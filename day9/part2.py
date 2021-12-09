from collections import Counter

text = open('input.txt').readlines()
data = [[int(y) for y in x.strip()] for x in text]

max = 10


def basin(i, j):
    next_node = None
    adj = [
        data[i - 1][j] if i > 0 else max,
        data[i + 1][j] if i < len(data) - 1 else max,
        data[i][j - 1] if j > 0 else max,
        data[i][j + 1] if j < len(data[i]) - 1 else max
    ]
    nodes = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    if data[i][j] > min(adj):
        next_node = nodes[adj.index(min(adj))]

    if next_node is None:
        return (i, j)
    return basin(*next_node)


basins = [basin(i, j) for i in range(len(data)) for j in range(len(data[i])) if data[i][j] != 9]

mul = 1
for _, i in Counter(basins).most_common(3):
    mul *= i
print(mul)
