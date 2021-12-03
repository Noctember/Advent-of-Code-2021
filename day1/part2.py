text = open('input.txt').readlines()
lines = [int(line.strip()) for line in text]
count = 0
prev = None
for i, num in enumerate(lines):
    group = sum(lines[i:i+3])
    if prev is not None:
        if group > prev:
            count += 1
    prev = group

print(f'There is {count} increments')
