text = open('input.txt').readlines()
num = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

amount = 0
for i, line in enumerate(text):
    line = line.split('|')[1]
    for j, digit in enumerate(line.strip().split(' ')):
        amount += 1 if len(digit) in num else 0

print(f'There are {amount} digits with unique amount of segments')
