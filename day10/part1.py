OPENERS = '{[(<'
CLOSERS = '}])>'
text = open('input.txt').readlines()

values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

expected = []
for i in range(len(text)):
    q = []
    for c in text[i]:
        if c in OPENERS:
            q.append(c)
        elif c in CLOSERS:
            if OPENERS.index(q.pop()) != CLOSERS.index(c):
                expected.append(c)
score = 0
for c in expected:
    score += values[c]
print(score)
