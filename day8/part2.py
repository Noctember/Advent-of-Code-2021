text = open('input.txt').readlines()

amount = 0
for i, line in enumerate(text):
    line = line.split('|')
    segments = [[] for _ in range(7)]
    for j, segment in enumerate(line[0].strip().split()):
        segments[len(segment) - 1].append(''.join(sorted(segment)))
    # DONE: 0, 1, 2, 3, 4, 6, 7, 8
    mapping = {
        segments[1][0]: '1',
        segments[2][0]: '7',
        segments[3][0]: '4',
        segments[6][0]: '8',
    }
    # 3 has 5 segments which contains all of 7's segments, diff = 2
    r3 = [digit for digit in segments[4] if len(set(digit) - set(segments[2][0])) == 2][0]
    mapping[r3] = '3'
    segments[4].remove(r3)

    # 6 has 6 segments which doesn't contains all of 7's segments, diff = 1
    r6 = [digit for digit in segments[5] if len(set(segments[2][0]) - set(digit)) == 1][0]
    mapping[r6] = '6'
    segments[5].remove(r6)

    # 9 has all of 5's segments + 1, so intersection is = 5
    r5, r9 = [(s5, s6) for s6 in segments[5] for s5 in segments[4] if len(set(s6) & set(s5)) == 5][0]
    mapping[r5] = '5'
    mapping[r9] = '9'
    segments[4].remove(r5)
    segments[5].remove(r9)

    # remaining
    mapping[segments[4].pop()] = '2'
    mapping[segments[5].pop()] = '0'

    num = ''.join([mapping[''.join(sorted(digit))] for digit in line[1].strip().split(' ')])
    amount += int(num)
print(f'Sum of all outputs is {amount}')
