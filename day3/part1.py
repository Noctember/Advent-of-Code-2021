data = open('input.txt').readlines()
data = [t.strip() for t in data]

gamma = ''
epsilon = ''
new = [[] for i in range(len(data[0]))]
for _, t in enumerate(data):
    for i, v in enumerate(t):
        new[i].append(v)

for i, num in enumerate(new):
    zeros = num.count('0')
    ones = num.count('1')
    print(ones, zeros)
    if zeros > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(f'Gamma: {gamma} Epsilon: {epsilon} Consumption: {int(gamma, 2) * int(epsilon, 2)}')
