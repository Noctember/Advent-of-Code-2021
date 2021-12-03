data = open('input.txt').readlines()
depth = 0
horizontal = 0
for i, num in enumerate(data):
    direction = num.split(' ')[0]
    distance = int(num.split(' ')[1])
    if direction == 'forward':
        horizontal += distance
    elif direction == 'up':
        depth -= distance
    elif direction == 'down':
        depth += distance
print(f'The depth is {depth} and distance is {horizontal}. Product is {depth*horizontal}')
