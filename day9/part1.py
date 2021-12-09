text = open('input.txt').readlines()
data = [[int(x) for x in y.strip()] for y in text]

risk_level = 0
max = 10
for i in range(len(data)):
    for j in range(len(data[0])):
        adj = [
            data[i - 1][j] if i > 0 else max,
            data[i + 1][j] if i < len(data) - 1 else max,
            data[i][j - 1] if j > 0 else max,
            data[i][j + 1] if j < len(data[0]) - 1 else max
        ]
        if data[i][j] < min(adj):
            risk_level += data[i][j] + 1
print(risk_level)
