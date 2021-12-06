text = open('input.txt').readlines()
initial = [int(x) for x in text[0].split(',')]
ending = []
for _ in range(80):
    for i in initial:
        new = i - 1
        if new < 0:
            new = 6
            ending.append(8)
        ending.append(new)
    initial = ending.copy()
    ending = []

print(f'Amount after 80 days: {len(initial)}')
