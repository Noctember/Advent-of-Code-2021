import queue

OPENERS = '{[(<'
CLOSERS = '}])>'
text = [x.strip() for x in open('input.txt').readlines()]

values = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

scores = []
for i in range(len(text)):
    q = []
    error = False
    score = 0
    for c in text[i]:
        if c in OPENERS:
            q.append(c)
        elif c in CLOSERS and c == CLOSERS[OPENERS.index(q[-1])]:
            q.pop()
        else:
            error = True
            break
    if len(q) and not error:
        for elem in q[::-1]:
            score *= 5
            score += values[elem]
        scores.append(score)

print(sorted(scores)[(len(scores) - 1) // 2])
