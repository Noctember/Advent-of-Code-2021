text = open('input.txt').readlines()
initial = [int(x) for x in text[0].split(',')]

fish = [0] * 9
for i in initial:
    fish[i] += 1

for i in range(256):
    six = fish.pop(0)
    fish[6] += six
    fish.append(six)
print(f'Amount after 256 days: {sum(fish)}')
