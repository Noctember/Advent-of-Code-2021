class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def points(self):
        if self.end[0] - self.start[0] != 0 and self.end[1] - self.start[1] != 0:
            return []
        elif self.end[0] - self.start[0] == 0:
            return [(self.start[0], y) for y in range(min(self.start[1], self.end[1]), max(self.start[1], self.end[1]) + 1)]
        else:
            return [(x, self.start[1]) for x in range(min(self.start[0], self.end[0]), max(self.start[0], self.end[0]) + 1)]

text = open('input.txt').readlines()
segments = []

for line in text:
    line = line.strip().split(' -> ')
    segments.append(Segment(eval(line[0]), eval(line[1])))

board = {}
for seg in segments:
    intersection = seg.points()
    for point in intersection:
        board[point] = board.setdefault(point, 0) + 1

i = 0
for v in board.values():
    if v > 1:
        i += 1
print(f'There are {i} points with at least 2 overlaps')
