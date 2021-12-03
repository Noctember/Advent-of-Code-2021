text = open('input.txt').readlines()
lines = [int(line.strip()) for line in text]
count = 0
for i, num in enumerate(lines):
    if i == 0:
        continue
    if num > lines[i-1]:
        count += 1
print(f'There is {count} increments')
