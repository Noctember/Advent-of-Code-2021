text = open('input.txt').read()
data = [int(x) for x in text.split(',')]
fuel = {}
for j in range(len(data)):
    for i in data:
        fuel[j] = fuel.setdefault(j, 0) + abs(i - j)
print(f'Lowest amount of fuel used: {min(fuel.values())}')
